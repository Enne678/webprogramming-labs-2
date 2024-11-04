from flask import Blueprint, render_template, request, make_response, redirect

lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name', 'аноним')
    age = request.cookies.get('age', 'неизвестный возраст')
    name_color = request.cookies.get('name_color')
    return render_template('lab3/lab3.html', name=name, name_color=name_color, age=age)

@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp

@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp

@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if not user:
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    if not age:
        errors['age'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)

@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')

@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'coffe':
        price = 120
    elif drink == 'black tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('lab3/pay.html', price=price)

@lab3.route('/lab3/success')
def success():
    price = request.args.get('price')
    return render_template('lab3/success.html', price=price)

@lab3.route('/lab3/settings')
def settings():
    color = request.args.get('color')
    bg_color = request.args.get('bg_color')
    font_size = request.args.get('font_size')
    font_family = request.args.get('font_family')
    
    if color or bg_color or font_size or font_family:
        resp = make_response(redirect('/lab3/settings'))
        if color:
            resp.set_cookie('color', color)
        if bg_color:
            resp.set_cookie('bg_color', bg_color)
        if font_size:
            resp.set_cookie('font_size', font_size)
        if font_family:
            resp.set_cookie('font_family', font_family)
        return resp
    
    color = request.cookies.get('color')
    bg_color = request.cookies.get('bg_color')
    font_size = request.cookies.get('font_size')
    font_family = request.cookies.get('font_family')
    
    return render_template('lab3/settings.html', color=color, bg_color=bg_color, font_size=font_size, font_family=font_family)

@lab3.route('/lab3/clear_settings_cookies')
def clear_settings_cookies():
    resp = make_response(redirect('/lab3/settings'))
    resp.delete_cookie('color')
    resp.delete_cookie('bg_color')
    resp.delete_cookie('font_size')
    resp.delete_cookie('font_family')
    resp.set_cookie('bg_color', '#ffffff')
    return resp

@lab3.route('/lab3/ticket', methods=['GET', 'POST'])
def ticket():
    if request.method == 'POST':
        fio = request.form['fio']
        bunk = request.form['bunk']
        bedding = 'on' if 'bedding' in request.form else 'off'
        luggage = 'on' if 'luggage' in request.form else 'off'
        age = int(request.form['age'])
        departure = request.form['departure']
        destination = request.form['destination']
        date = request.form['date']
        insurance = 'on' if 'insurance' in request.form else 'off'

        if age < 18:
            ticket_type = "Детский билет"
            price = 700
        else:
            ticket_type = "Взрослый билет"
            price = 1000

        if bunk in ['нижняя', 'нижняя боковая']:
            price += 100
        if bedding == 'on':
            price += 75
        if luggage == 'on':
            price += 250
        if insurance == 'on':
            price += 150

        return render_template('lab3/ticket.html', fio=fio, bunk=bunk, bedding=bedding, luggage=luggage, age=age, departure=departure, destination=destination, date=date, insurance=insurance, price=price, ticket_type=ticket_type)
    
    return render_template('lab3/ticket_form.html')

cars = [
    {'name': 'Toyota Camry', 'price': 2500000, 'color': 'White', 'brand': 'Toyota'},
    {'name': 'Honda Accord', 'price': 2400000, 'color': 'Black', 'brand': 'Honda'},
    {'name': 'BMW 3 Series', 'price': 3500000, 'color': 'Blue', 'brand': 'BMW'},
    {'name': 'Audi A4', 'price': 4000000, 'color': 'Red', 'brand': 'Audi'},
    {'name': 'Mercedes-Benz C-Class', 'price': 4200000, 'color': 'Silver', 'brand': 'Mercedes-Benz'},
    {'name': 'Ford Fusion', 'price': 2200000, 'color': 'Gray', 'brand': 'Ford'},
    {'name': 'Chevrolet Malibu', 'price': 2100000, 'color': 'White', 'brand': 'Chevrolet'},
    {'name': 'Nissan Altima', 'price': 2300000, 'color': 'Black', 'brand': 'Nissan'},
    {'name': 'Hyundai Sonata', 'price': 2400000, 'color': 'Blue', 'brand': 'Hyundai'},
    {'name': 'Kia Optima', 'price': 2350000, 'color': 'Red', 'brand': 'Kia'},
    {'name': 'Mazda 6', 'price': 2700000, 'color': 'Silver', 'brand': 'Mazda'},
    {'name': 'Subaru Legacy', 'price': 2600000, 'color': 'Gray', 'brand': 'Subaru'},
    {'name': 'Volkswagen Passat', 'price': 2800000, 'color': 'White', 'brand': 'Volkswagen'},
    {'name': 'Lexus ES', 'price': 4500000, 'color': 'Black', 'brand': 'Lexus'},
    {'name': 'Infiniti Q50', 'price': 4300000, 'color': 'Blue', 'brand': 'Infiniti'},
    {'name': 'Acura TLX', 'price': 3600000, 'color': 'Red', 'brand': 'Acura'},
    {'name': 'Tesla Model 3', 'price': 5000000, 'color': 'White', 'brand': 'Tesla'},
    {'name': 'Cadillac CT5', 'price': 4700000, 'color': 'Black', 'brand': 'Cadillac'},
    {'name': 'Jaguar XE', 'price': 4800000, 'color': 'Blue', 'brand': 'Jaguar'},
    {'name': 'Volvo S60', 'price': 4600000, 'color': 'Red', 'brand': 'Volvo'}
]

@lab3.route('/lab3/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        min_price = int(request.form['min_price'])
        max_price = int(request.form['max_price'])

        filtered_cars = [car for car in cars if min_price <= car['price'] <= max_price]

        return render_template('lab3/search_results.html', cars=filtered_cars, min_price=min_price, max_price=max_price)
    return render_template('lab3/search_form.html')