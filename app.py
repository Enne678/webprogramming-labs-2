from flask import Flask, redirect, url_for, render_template, request
from lab1 import lab1
from flask import Flask

app = Flask(__name__)
app.register_blueprint(lab1)

if __name__ == "__main__":
    app.run()

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route('/lab2/a')
def a():
    return 'без слэша'

@app.route('/lab2/a/')
def a2():
    return 'со слэшем'

flower_list = [
    {'name': 'роза', 'price': 50},
    {'name': 'тюльпан', 'price': 30},
    {'name': 'незабудка', 'price': 20},
    {'name': 'ромашка', 'price': 10}
]

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return "такого цветка нет", 404
    else:
        return render_template('flower.html', flower=flower_list[flower_id])

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
    name = 'Алексей Миллер'
    lab_number = '2'
    group = 'ФБИ-24'
    course = '3'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]
    return render_template('example.html', name=name, lab_number=lab_number, group=group,
                            course=course, fruits=fruits)

@app.route('/lab2/')
def lab():
    return render_template('lab2.html')

@app.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase = phrase)

@app.route('/lab2/add_flower/')
def add_flower_missing_name():
    return "вы не задали имя цветка", 400

@app.route('/lab2/all_flowers')
def all_flowers():
    return render_template('all_flowers.html', flowers=flower_list, count=len(flower_list))

@app.route('/lab2/clear_flowers')
def clear_flowers():
    global flower_list
    flower_list = []
    return redirect(url_for('all_flowers'))

@app.route('/lab2/calc/')
def calc_default():
    return redirect('/lab2/calc/1/1')

@app.route('/lab2/calc/<int:a>')
def calc_single_param(a):
    return redirect(f'/lab2/calc/{a}/1')

@app.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    result = {
        'sum': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b if b != 0 else 'undefined',
        'power': a ** b
    }
    return render_template('calc.html', a=a, b=b, result=result)

@app.route('/lab2/books')
def books():
    books_list = [
        {'author': 'Автор 1', 'title': 'Книга 1', 'genre': 'Жанр 1', 'pages': 100},
        {'author': 'Автор 2', 'title': 'Книга 2', 'genre': 'Жанр 2', 'pages': 150},
        {'author': 'Автор 3', 'title': 'Книга 3', 'genre': 'Жанр 3', 'pages': 200},
        {'author': 'Автор 4', 'title': 'Книга 4', 'genre': 'Жанр 4', 'pages': 250},
        {'author': 'Автор 5', 'title': 'Книга 5', 'genre': 'Жанр 5', 'pages': 300},
        {'author': 'Автор 6', 'title': 'Книга 6', 'genre': 'Жанр 6', 'pages': 350},
        {'author': 'Автор 7', 'title': 'Книга 7', 'genre': 'Жанр 7', 'pages': 400},
        {'author': 'Автор 8', 'title': 'Книга 8', 'genre': 'Жанр 8', 'pages': 450},
        {'author': 'Автор 9', 'title': 'Книга 9', 'genre': 'Жанр 9', 'pages': 500},
        {'author': 'Автор 10', 'title': 'Книга 10', 'genre': 'Жанр 10', 'pages': 550}
    ]
    return render_template('books.html', books=books_list)

@app.route('/lab2/objects')
def objects():
    objects_list = [
        {'name': 'Клубника', 'description': 'Сочная и сладкая ягода, идеально подходит для десертов.', 'image': 'strawberry.jpg'},
        {'name': 'Малина', 'description': 'Ароматная ягода с насыщенным вкусом, отлично подходит для варенья.', 'image': 'raspberry.jpg'},
        {'name': 'Черника', 'description': 'Полезная и вкусная ягода, богатая витаминами и антиоксидантами.', 'image': 'blueberry.jpg'},
        {'name': 'Смородина', 'description': 'Кисло-сладкая ягода, прекрасный источник витамина С.', 'image': 'currant.jpg'},
        {'name': 'Крыжовник', 'description': 'Кисло-сладкая ягода с тонкой кожицей, идеальна для компотов и джемов.', 'image': 'gooseberry.jpg'}
    ]
    return render_template('objects.html', objects=objects_list)

@app.route('/lab2/flowers_list')
def flowers_list():
    return render_template('all_flowers.html', flowers=flower_list, count=len(flower_list))

@app.route('/lab2/add_new_flower', methods=['POST'])
def add_new_flower():
    name = request.form['name']
    price = request.form['price']
    flower_list.append({'name': name, 'price': float(price)})
    return redirect(url_for('flowers_list'))

@app.route('/lab2/delete_specific_flower/<int:flower_id>')
def delete_specific_flower(flower_id):
    if flower_id >= len(flower_list):
        return "такого цветка нет", 404
    else:
        flower_list.pop(flower_id)
        return redirect(url_for('flowers_list'))
    
if __name__ == "__main__":
    app.run(debug=True)

