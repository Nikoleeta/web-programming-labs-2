from flask import Blueprint, render_template, request, make_response
lab4=Blueprint('lab4', __name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')


@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'nikoleta' and password == '1':
        return render_template('success2.html')
    error = 'Неверные логин и/или пароль'
    if username == '':
        error='Вы не ввели логин'
    if password == '':
        error='Вы не ввели пароль'

    return render_template('login.html',error=error,
                           username=username, password=password)


@lab4.route('/lab4/fridge',  methods=['GET', 'POST'])
def fridge():
    if request.method =='GET':
        return render_template('fridge.html')
    
    temp = request.form.get('temp')   
    if temp == "":
        message = 'Ошибка: не задана температура'
    else:
        temp = int(request.form.get('temp'))
        if temp < -12:
            message = 'Не удалось установить температуру - слишком низкое значение'
        if temp > -1:
            message = 'Не удалось установить температуру - слишком высокое значение'
        if temp >= -12 and temp <=-9:
            message = f'Установлена температура: {temp}℃'+'❄️❄️❄️'
        if temp >= -8 and temp <=-5:
            message = f'Установлена температура: {temp}℃'+'❄️❄️'
        if temp >= -4 and temp <=-1:
            message = f'Установлена температура: {temp}℃'+'❄️'
        
    return render_template('fridge.html', temp=temp, message=message)


@lab4.route('/lab4/seed',  methods=['GET', 'POST'])
def seed():
    if request.method == 'GET':
        return render_template('seed.html')

    price = 0
    seed = request.form.get('seed')
    ves = request.form.get('ves')

    if ves=='':
        message='Не введен вес'
        return render_template('seed.html', message=message,ves=ves)
    else:
        ves = int(request.form.get('ves'))
        if seed == 'Ячмень':
            price = price + 12000*ves
        elif seed=='Пшеница':
            price= price+8700*ves
        elif seed=='Рожь':
            price=price+14000*ves
        else:
            price=price+8500*ves

    if ves <=0:
        message='Неверное значение'
        return render_template('seed.html', message=message,ves=ves)
    if ves > 500:
        message='У нас столько нет'
        return render_template('seed.html', message=message,ves=ves)

    if ves>50:
        price=int(price - (price*10)/100)
        mes='Скидка 10% за большой объем'
    return render_template('seed.html', seed=seed, 
                           ves=ves, price=price,mes=mes)



@lab4.route('/lab4/cookies', methods=['GET', 'POST'])
def cookies():
    resp = make_response(render_template('cookies.html'))
    color = request.form.get('color')
    b_color = request.form.get('background-color')
    f_size = request.form.get('font-size')
    if color and b_color and f_size:
        resp.set_cookie('color', color)
        resp.set_cookie('background-color', b_color)
        resp.set_cookie('font-size', f"{f_size}px")
        return resp
    return 'waiting for parameters'
    