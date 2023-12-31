from flask import Blueprint, render_template, request
import math
lab3=Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')


@lab3.route('/lab3/forms')
def form1():
    errors={}
    user=request.args.get('user')
    if user == '':
        errors['user']='Fill in the field'

    age=request.args.get('age')
    if age =='':
        errors['age']='Fill in the field'

    sex=request.args.get('sex')
    return render_template('form.html', user=user, 
                           age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
   return render_template('order.html')

@lab3.route('/lab3/pay')
def pay():
    price=0
    drink=request.args.get('drink')
    if drink=='coffee':
        price=120
    elif drink=='black tea':
        price =80
    else:
        price=70
    
    if request.args.get('milk')=='on':
        price+=30
    if request.args.get('sugar')=='on':
       price+=10
       
    return render_template('pay.html', price=price)


@lab3.route('/lab3/success')
def suc():
    return render_template('success.html')


@lab3.route('/lab3/ticket')
def tick():
    errors={}

    user=request.args.get('user')
    if user == '':
        errors['user']='Fill in the field'

    type=request.args.get('type')
    if type == '':
        errors['type']='Fill in the field'

    seat=request.args.get('seat')
    if seat == '':
        errors['seat']='Fill in the field'

    lugagge=request.args.get('lugagge')
    if lugagge == '':
        errors['lugagge']='Fill in the field'

    age=request.args.get('age') 
    if age == '':
        errors['age']='Fill in the field'

    date=request.args.get('date')
    if date == '':
        errors['date']='Fill in the field'

    departure=request.args.get('departure')
    if departure == '':
        errors['departure']='Fill in the field'

    destination=request.args.get('destination')
    if destination == '':
        errors['destination']='Fill in the field'

    
    return render_template('ticket.html', errors=errors, user=user,
                          type=type, seat=seat, lugagge=lugagge,
                          age=age, date=date,departure=departure,
                          destination=destination)


@lab3.route('/lab3/buy')
def ticket():
    return render_template('ticketbuy.html')


@lab3.route('/lab3/zac')
def zac():
    x = float (request.args.get('x'))
    n = int (request.args.get('n'))
 
    def fac (n):
        res=1
        for i in range (1, n+1):
            res*=i
        return res
    
    result=1
    sign=-1
    for i in range (1, n+1):    
       y=(sign*x**(2*i+1))/(fac(2*n+1))
       result += y
       sign*=-1
           
    return f"result={result}, n={n}, x={x}" 


@lab3.route('/lab3/zac2')
def zac2():
    res=0
    a,b,c,d = [request.args.get('a'), request.args.get('b'),
           request.args.get('c'), request.args.get('d')]   
    if a==b==c:
        res=4,
    elif  b==c==d:
        res=1,
    elif a==c==d:
        res=2
    else:
        res=3

    return f"res={res}"

