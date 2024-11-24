from flask import Blueprint, render_template, request, redirect, session

lab4 = Blueprint('lab4', __name__)
tree_count = 0

@lab4.route('/lab4/')
def lab():
    return render_template('lab4/lab4.html')

@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')

@lab4.route('/lab4/div', methods=['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены!')

    try:
        x1 = int(x1)
        x2 = int(x2)
    except ValueError:
        return render_template('lab4/div.html', error='Оба поля должны содержать числа!')

    if x2 == 0:
        return render_template('lab4/div.html', error='Делить на ноль нельзя!')

    result = x1 / x2
    return render_template('lab4/div.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/add-form')
def add_form():
    return render_template('lab4/add-form.html')

@lab4.route('/lab4/add', methods=['POST'])
def add():
    x1 = request.form.get('x1', '0')
    x2 = request.form.get('x2', '0')
    try:
        x1 = int(x1)
        x2 = int(x2)
    except ValueError:
        return render_template('add.html', error='Оба поля должны содержать числа!')
    result = x1 + x2
    return render_template('lab4/add.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/multiply-form')
def multiply_form():
    return render_template('lab4/multiply-form.html')

@lab4.route('/lab4/multiply', methods=['POST'])
def multiply():
    x1 = request.form.get('x1', '1')
    x2 = request.form.get('x2', '1')
    try:
        x1 = int(x1)
        x2 = int(x2)
    except ValueError:
        return render_template('multiply.html', error='Оба поля должны содержать числа!')
    result = x1 * x2
    return render_template('lab4/multiply.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/subtract-form')
def subtract_form():
    return render_template('lab4/subtract-form.html')

@lab4.route('/lab4/subtract', methods=['POST'])
def subtract():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('subtract.html', error='Оба поля должны быть заполнены!')
    try:
        x1 = int(x1)
        x2 = int(x2)
    except ValueError:
        return render_template('subtract.html', error='Оба поля должны содержать числа!')
    result = x1 - x2
    return render_template('lab4/subtract.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/power-form')
def power_form():
    return render_template('lab4/power-form.html')

@lab4.route('/lab4/power', methods=['POST'])
def power():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/power.html', error='Оба поля должны быть заполнены!')
    try:
        x1 = int(x1)
        x2 = int(x2)
    except ValueError:
        return render_template('lab4/power.html', error='Оба поля должны содержать числа!')
    
    if x1 == 0 and x2 == 0:
        result = 1  
    else:
        result = x1 ** x2
    
    return render_template('lab4/power.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/tree', methods=['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'POST':
        operation = request.form.get('operation')

        if operation == 'cut' and tree_count > 0:
            tree_count -= 1
        elif operation == 'plant' and tree_count < 10:
            tree_count += 1

        return redirect('/lab4/tree')
    return render_template('lab4/tree.html', tree_count=tree_count)

users = [
    {'login': 'alex', 'password': '123', 'name': 'Алексей Миллер', 'gender': 'M'},
    {'login': 'bob', 'password': '555', 'name': 'Роберт Браун', 'gender': 'M'}
]

@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'login' in session:
            authorized = True
            login = session['login']
            for user in users:
                if user['login'] == login:
                    name = user['name']
                    break
        else:
            authorized = False
            login = ''
            name = ''
        return render_template('lab4/login.html', authorized=authorized, login=login, name=name)
    
    login = request.form.get('login')
    password = request.form.get('password')

    if not login:
        error = 'Не введён логин'
        return render_template('lab4/login.html', error=error, authorized=False)
    if not password:
        error = 'Не введён пароль'
        return render_template('lab4/login.html', error=error, authorized=False)

    for user in users:
        if login == user['login'] and password == user['password']:
            session['login'] = login
            return redirect('/lab4/login')
            
    error = 'Неверные логин и/или пароль'
    return render_template('lab4/login.html', error=error, authorized=False, login=login)

@lab4.route('/lab4/logout', methods=['POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')

@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge():
    if request.method == 'POST':
        temperature = request.form.get('temperature')
        if temperature is None or temperature == '':
            error = 'Ошибка: не задана температура'
            return render_template('lab4/fridge.html', error=error)
        
        try:
            temperature = float(temperature)
        except ValueError:
            error = 'Некорректное значение температуры'
            return render_template('lab4/fridge.html', error=error)
        
        if temperature < -12:
            error = 'Не удалось установить температуру — слишком низкое значение'
            return render_template('lab4/fridge.html', error=error)
        elif temperature > -1:
            error = 'Не удалось установить температуру — слишком высокое значение'
            return render_template('lab4/fridge.html', error=error)
        elif -12 <= temperature <= -9:
            message = f'Установлена температура: {temperature}°С'
            snowflakes = '❄️❄️❄️'
        elif -8 <= temperature <= -5:
            message = f'Установлена температура: {temperature}°С'
            snowflakes = '❄️❄️'
        elif -4 <= temperature <= -1:
            message = f'Установлена температура: {temperature}°С'
            snowflakes = '❄️'

        return render_template('lab4/fridge.html', message=message, snowflakes=snowflakes)
    
    return render_template('lab4/fridge.html')

@lab4.route('/lab4/grain-order', methods=['GET', 'POST'])
def grain_order():
    prices = {
        'ячмень': 12345,
        'овёс': 8522,
        'пшеница': 8722,
        'рожь': 14111
    }

    if request.method == 'POST':
        grain = request.form.get('grain')
        weight = request.form.get('weight')

        if weight is None or weight == '':
            error = 'Ошибка: не указан вес'
            return render_template('lab4/grain-order.html', error=error)

        try:
            weight = float(weight)
        except ValueError:
            error = 'Некорректное значение веса'
            return render_template('lab4/grain-order.html', error=error)
        
        if weight <= 0:
            error = 'Ошибка: вес должен быть больше нуля'
            return render_template('lab4/grain-order.html', error=error)
        elif weight > 500:
            error = 'Ошибка: такого объёма сейчас нет в наличии'
            return render_template('lab4/grain-order.html', error=error)
        
        total_cost = prices[grain] * weight
        discount = 0
        if weight > 50:
            discount = 0.1 * total_cost
            total_cost -= discount
            discount_message = f'Применена скидка за большой объём: {discount:.2f} руб'
        else:
            discount_message = None
        
        message = f'Заказ успешно сформирован. Вы заказали {grain}. Вес: {weight} т. Сумма к оплате: {total_cost:.2f} руб'
        return render_template('lab4/grain-order.html', message=message, discount_message=discount_message)
    
    return render_template('lab4/grain-order.html')