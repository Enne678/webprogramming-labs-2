from flask import Blueprint, render_template, request, redirect, session
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import generate_password_hash, check_password_hash

lab5 = Blueprint('lab5', __name__)

@lab5.route('/lab5/')
def lab():
    login = session.get('login')
    if not login:
        return render_template('lab5/lab5.html', login=None, articles=[])

    conn, cur = db_connect()

    try:
        cur.execute("SELECT id FROM users WHERE login = %s;", (login,))
        user = cur.fetchone()

        if not user:
            return "Пользователь не найден", 404

        user_id = user['id']

        cur.execute("SELECT * FROM articles WHERE user_id = %s;", (user_id,))
        articles = cur.fetchall()
    except Exception as e:
        return f"Ошибка при получении статей: {e}", 500
    finally:
        db_close(conn, cur)

    return render_template('lab5/lab5.html', login=login, articles=articles)

def db_connect():
    conn = psycopg2.connect(
        host='127.0.0.1',
        database='alex_miller_knowledge_base',
        user='alex_miller_knowledge_base',
        password='123',
        client_encoding='UTF8'
    )
    cur = conn.cursor(cursor_factory=RealDictCursor)
    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

def update_passwords():
    conn, cur = db_connect()

    cur.execute("SELECT id, password FROM users;")
    users = cur.fetchall()

    for user in users:
        user_id, password = user
        password_hash = generate_password_hash(password)
        cur.execute("UPDATE users SET password = %s WHERE id = %s;", (password_hash, user_id))

    db_close(conn, cur)

if __name__ == "__main__":
    update_passwords()
    print("Пароли успешно обновлены на хеши.")

@lab5.route('/lab5/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab5/register.html')

    login = request.form.get('login')
    password = request.form.get('password')

    if not (login or password):
        return render_template('lab5/register.html', error='Заполните все поля')

    conn, cur = db_connect()

    cur.execute("SELECT login FROM users WHERE login=%s;", (login,))
    if cur.fetchone():
        db_close(conn, cur)
        return render_template('lab5/register.html', error='Такой пользователь уже существует')

    password_hash = generate_password_hash(password)
    cur.execute("INSERT INTO users (login, password) VALUES (%s, %s);", (login, password_hash))

    db_close(conn, cur)
    return render_template('lab5/success.html', login=login)

@lab5.route('/lab5/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab5/login.html')

    login = request.form.get('login')
    password = request.form.get('password')

    if not (login or password):
        return render_template('lab5/login.html', error='Заполните все поля')

    conn, cur = db_connect()

    cur.execute("SELECT * FROM users WHERE login=%s;", (login, ))    
    user = cur.fetchone()

    if not user:
        db_close(conn, cur)
        return render_template('lab5/login.html', error='Логин и/или пароль неверны')

    if not check_password_hash(user['password'], password):
        db_close(conn, cur)
        return render_template('lab5/login.html', error='Логин и/или пароль неверны')

    session['login'] = login
    db_close(conn, cur)
    return render_template('lab5/success_login.html', login=login)

@lab5.route('/lab5/delete_user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'GET':
        return render_template('lab5/delete_user.html')
    elif request.method == 'POST':
        login = session.get('login')
        if not login:
            return redirect('/lab5/login')

        user_to_delete = request.form.get('user_to_delete')

        if not user_to_delete:
            return "Логин пользователя не указан", 400

        conn, cur = db_connect()

        try:
            cur.execute("DELETE FROM users WHERE login = %s;", (user_to_delete,))
            conn.commit()
        except Exception as e:
            conn.rollback()
            return f"Ошибка при удалении пользователя: {e}", 500
        finally:
            db_close(conn, cur)

        return f"Пользователь {user_to_delete} успешно удалён", 200

@lab5.route('/lab5/create', methods=['GET', 'POST'])
def create():
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')

    if request.method == 'GET':
        return render_template('lab5/create_article.html')

    title = request.form.get('title')
    article_text = request.form.get('article_text')

    if not (title or article_text):
        return render_template('lab5/create_article.html', error='Заполните все поля')

    conn, cur = db_connect()

    try:
        cur.execute("SELECT id FROM users WHERE login = %s;", (login,))
        user = cur.fetchone()
        if not user:
            return "Пользователь не найден", 404

        user_id = user['id']

        cur.execute(
            "INSERT INTO articles (user_id, title, article_text) VALUES (%s, %s, %s);",
            (user_id, title, article_text)
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        return f"Ошибка при создании статьи: {e}", 500
    finally:
        db_close(conn, cur)

    return redirect('/lab5')

@lab5.route('/lab5/delete_article/<int:article_id>', methods=['POST'])
def delete_article(article_id):
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')

    conn, cur = db_connect()

    try:
        cur.execute("SELECT user_id FROM articles WHERE id = %s;", (article_id,))
        article = cur.fetchone()

        if not article:
            return "Статья не найдена", 404

        cur.execute("SELECT id FROM users WHERE login = %s;", (login,))
        user = cur.fetchone()

        if not user or article['user_id'] != user['id']:
            return "У вас нет прав на удаление этой статьи", 403

        cur.execute("DELETE FROM articles WHERE id = %s;", (article_id,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        return f"Ошибка при удалении статьи: {e}", 500
    finally:
        db_close(conn, cur)

    return redirect('/lab5')

@lab5.route('/lab5/list')
def list():
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')

    conn, cur = db_connect()

    cur.execute("SELECT id FROM users WHERE login = %s;", (login,))
    user = cur.fetchone()

    if not user:
        return "Пользователь не найден", 404

    user_id = user['id']

    cur.execute("SELECT * FROM articles WHERE user_id = %s;", (user_id,))
    articles = cur.fetchall()

    db_close(conn, cur)

    return render_template('lab5/articles.html', articles=articles)