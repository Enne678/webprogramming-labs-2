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
    return """
<!doctype html>
<html>
    <head>
        <title>Миллер Алексей Евгеньевич, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <h1>web-сервер на flask</h1>
        <p>Flask — фреймворк для создания веб-приложений на языке программирования Python, использующий набор инструментов Werkzeug, а также шаблонизатор Jinja2. Относится к категории так называемых микрофреймворков — минималистичных каркасов веб-приложений, сознательно предоставляющих лишь самые базовые возможности.</p>
        <footer>
            © Алексей Миллер, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""


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

if __name__ == "__main__":
    app.run(debug=True)