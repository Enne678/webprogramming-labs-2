from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
        <nav>
            <ul>
                <li><a href="/lab1">Первая лабораторная</a></li>
            </ul>
        </nav>
        <footer>
            © Алексей Миллер, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""

@app.route("/lab1")
def lab1():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Миллер Алексей Евгеньевич, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <h1>web-сервер на flask</h1>
        <p>Flask — фреймворк для создания веб-приложений на языке программирования Python...</p>
        <a href="/menu">Вернуться в меню</a>
        <h2>Реализованные роуты</h2>
        <ul>
            <li><a href="/lab1/oak">/lab1/oak</a></li>
            <li><a href="/lab1/student">/lab1/student</a></li>
            <li><a href="/lab1/python">/lab1/python</a></li>
            <li><a href="/lab1/custom">/lab1/custom</a></li>
        </ul>
        <footer>
            © Алексей Миллер, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route('/lab1/oak')
def oak():
    return '''
    <!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''" width="854" height="480">
    </body>
</html>
'''

@app.route('/lab1/student')
def student():
    return '''
    <!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, Информация о студенте
        </header>
        <h1>Миллер Алексей Евгеньевич</h1>
        <img src="''' + url_for('static', filename='nstu_logo.png') + '''" width="200" height="200">
        <footer>
            © Алексей Миллер, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route('/lab1/python')
def python_info():
    return '''
    <!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            Информация о Python
        </header>
        <h1>Язык программирования Python</h1>
        <p>Python — высокоуровневый язык программирования, известный своей простотой и читаемостью кода...</p>
        <p>Python используется для веб-разработки, анализа данных, искусственного интеллекта, автоматизации задач и многого другого.</p>
        <img src="''' + url_for('static', filename='python_logo.png') + '''" width="200" height="200">
        <footer>
            © Алексей Миллер, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route('/lab1/custom')
def custom():
    return '''
    <!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            Персональный выбор темы
        </header>
        <h1>История Python</h1>
        <p>Python был создан Гвидо ван Россумом в конце 1980-х годов как преемник ABC. Python разработан для улучшения продуктивности...</p>
        <p>Современный Python используется в различных сферах, таких как наука, машинное обучение, веб-разработка, и автоматизация.</p>
        <img src="''' + url_for('static', filename='python_history.png') + '''" width="200" height="200">
        <footer>
            © Алексей Миллер, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

if __name__ == "__main__":
    app.run(debug=True)