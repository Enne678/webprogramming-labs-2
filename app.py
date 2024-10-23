from flask import Flask, redirect, url_for, render_template, request
from lab1 import lab1
from lab2 import lab2
app = Flask(__name__)

app.register_blueprint(lab1)
app.register_blueprint(lab2)

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
                <li><a href="/lab1/">Первая лабораторная</a></li>
                <li><a href="/lab2/">Вторая лабораторная</a></li>
            </ul>
        </nav>
        <footer>
            &copy; Алексей Миллер, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>"""

@app.errorhandler(404)
def page_not_found(error):
    return "Страница не найдена", 404

@app.errorhandler(500)
def server_error(error):
    return "Ошибка сервера", 500

if __name__ == "__main__":
    app.run(debug=True)