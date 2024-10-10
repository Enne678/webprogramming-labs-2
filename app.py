from flask import Flask, redirect, url_for, render_template
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
            &copy; Алексей Миллер, ФБИ-24, 3 курс, 2024
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
        <p>Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов
        веб-приложений, сознательно предоставляющих лишь самые базовые возможности.</p>
        <a href="/menu">Вернуться в меню</a>
        <h2>Реализованные роуты</h2>
        <ul>
            <li><a href="/lab1/oak">/lab1/oak</a></li>
            <li><a href="/lab1/student">/lab1/student</a></li>
            <li><a href="/lab1/python">/lab1/python</a></li>
            <li><a href="/lab1/custom">/lab1/custom</a></li>
        </ul>
        <footer>
            &copy; Алексей Миллер, ФБИ-24, 3 курс, 2024
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
            &copy; Алексей Миллер, ФБИ-24, 3 курс, 2024
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
        <p>Python — высокоуровневый язык программирования, известный своей простотой и читаемостью кода. Благодаря минималистичному синтаксису, он позволяет разработчикам сосредоточиться на решении задач, а не на сложных деталях реализации. Такой подход делает Python особенно популярным среди новичков, а также среди опытных программистов, которым важна скорость разработки и поддержка проектов.</p>
        <p>Кроме того, Python обладает богатой стандартной библиотекой, включающей инструменты для работы с текстом, данными, интернет-протоколами и многим другим. Благодаря этому, Python широко применяется в различных областях, таких как веб-разработка, анализ данных, машинное обучение, автоматизация процессов и создание приложений. Гибкость Python делает его универсальным инструментом для решения практически любых задач.</p>
        <p>Python используется для веб-разработки, анализа данных, искусственного интеллекта, автоматизации задач и многого другого.</p>
        <img src="''' + url_for('static', filename='python_logo.png') + '''" width="200" height="200">
        <footer>
            &copy; Алексей Миллер, ФБИ-24, 3 курс, 2024
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
        <p>Python был создан Гвидо ван Россумом в конце 1980-х годов как преемник языка ABC. Основная цель создания Python заключалась в том, чтобы предложить более простой и эффективный инструмент для программирования, который бы устранял недостатки других языков, таких как сложность синтаксиса и ограниченные возможности. Python сразу приобрел популярность благодаря своей простоте, позволяя программистам писать понятный и легко поддерживаемый код.</p>
        <p>Python разработан для улучшения продуктивности разработчиков за счёт высокого уровня абстракции и лаконичного синтаксиса. Одной из его ключевых особенностей стала поддержка множества парадигм программирования, включая объектно-ориентированное, процедурное и функциональное программирование. Это позволяет создавать как небольшие скрипты, так и крупные масштабируемые приложения, что делает Python универсальным инструментом для разработчиков различных уровней.</p>
        <p>Современный Python используется в различных сферах, таких как наука, машинное обучение, веб-разработка, и автоматизация.</p>
        <img src="''' + url_for('static', filename='python_history.png') + '''" width="200" height="200">
        <footer>
            &copy; Алексей Миллер, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route('/lab2/a')
def a():
    return 'без слэша'

@app.route('/lab2/a/')
def a2():
    return 'со слэшем'

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return "такого цветка нет", 404
    else:
        return "цветок: " + flower_list[flower_id]

@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.append(name)
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Добавлен новый цветок</h1>
    <p>Название нового цветка: {name} </p>
    <p>Всего цветов: {len(flower_list)}</p>
    <p>Полный список: {flower_list}</p>
    </body>
</html>
'''

@app.route('/lab2/example')
def example():
    return render_template('example.html')

if __name__ == "__main__":
    app.run(debug=True)

