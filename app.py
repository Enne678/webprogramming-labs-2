from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
    return """
<!doctype html>
<html>
    <head>
        <title>Миллер Алексей Евгеньевич, лабораторная 1</title>
     </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </heder>

        <h1>web-сервер на flask</h1>

        <footer>
            &copy; Алексей Миллер, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""