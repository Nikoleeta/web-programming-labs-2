from flask import Blueprint, redirect, url_for, render_template
lab2=Blueprint('lab2',__name__)


@lab2.route('/lab2/')
def labb2():
    return render_template('lab2.html')


@lab2.route('/lab2/example')
def example():
    name, num, course, group='Nikoleta Kosareva', 2, '3 course', 'FBI-12'
    fruits=[
        {'name':'apples','price':100},
        {'name':'pears', 'price':120},
        {'name':'oranges', 'price':80},
        {'name':'mango', 'price':321},
        {'name':'tangerines', 'price':95}
    ]

    books=[
        {'author': 'E.Maria Remarque', 'bookname':'"Three Comrades"', 
        'genre': 'war novel', 'quantity': 480},
        {'author': 'Kristina Stark', 'bookname':'"Wings"', 
        'genre': 'novel','quantity': 480},
        {'author': 'D. Gherbert Lawrence', 'bookname':'"Lady Chatterleys lover"', 
        'genre': 'novel', 'quantity': 448},
        {'author': 'F. Hodgson Burnett', 'bookname':'"Secret Garden"', 
        'genre': 'novel','quantity': 150},
        {'author': 'Lev Tolstoy',  'bookname':'"Anna Karenina"', 
        'genre': 'novel','quantity': 850},
        {'author': 'Anne Bronte', 'bookname':'"The Tenant of Wildfell Hall"', 
        'genre': 'novel','quantity': 640},
        {'author': 'L. May Alcott', 'bookname':'"Little Women"', 
        'genre': 'novel','quantity': 384},
        {'author': 'Fedor Dostoevskiy',  'bookname':'"Crime and punishment"', 
        'genre': 'socio-pccychological novel','quantity': 592},
        {'author': 'Fedor Dostoevskiy',  'bookname':'"White nights"', 
        'genre': 'novel','quantity': 70},
        {'author': 'Arthur Hailey',  'bookname':'"Hotel"', 
        'genre': 'novel','quantity': 500}]

    return render_template('example.html', 
            num=num, name=name, course=course, 
            group=group, fruits=fruits, books=books)
   
@lab2.route('/lab2/studying')
def lab2st():
    return render_template('studying.html')


@lab2.route('/lab2/zac')
def zac():
    a,b,c = 3,4,5
    if a<b<c:
        a=a*2   
        b=b*2
        c=c*2 
    else:
        a=a
        b=b
        c=c
    return f"a={a}, b={b}, c={c}"

@lab2.route('/lab2/zac2')
def zac1():
    n=2
    k=4
    return str(n)*k


@lab2.route('/lab2/zac3')
def zac2():
    n=5
    k=1
    sum=0
    for i in range(1,n+1):
        sum=sum+i**k
    return f"sum={sum}"