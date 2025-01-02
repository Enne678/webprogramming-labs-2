import psycopg2
from werkzeug.security import generate_password_hash
from psycopg2.extras import RealDictCursor

def db_connect():
    conn = psycopg2.connect(
        host='127.0.0.1',
        database='alex_miller_knowledge_base',
        user='alex_miller_knowledge_base',
        password='123'
    )
    cur = conn.cursor(cursor_factory=RealDictCursor)
    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

def update_passwords():
    conn, cur = db_connect()

    # Получаем всех пользователей
    cur.execute("SELECT id, password FROM users;")
    users = cur.fetchall()

    for user in users:
        user_id, password = user
        # Генерируем хеш пароля
        password_hash = generate_password_hash(password)
        # Обновляем запись в базе данных
        cur.execute("UPDATE users SET password = %s WHERE id = %s;", (password_hash, user_id))

    db_close(conn, cur)

if __name__ == "__main__":
    update_passwords()
    print("Пароли успешно обновлены на хеши.")