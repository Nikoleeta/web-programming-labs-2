from flask import Flask, redirect, url_for
app=Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect ("/menu", code=302)

@app.route("/lab1")
def lab1():
    return"""
<!doctype html>
<html>
    <head>
        <title> Косарева Николета Вячеславовна, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа №1
        </header>

        <p>Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов
        веб-приложений, сознательно предоставляющих лишь 
        самые базовые возможности</p>

        <a href="http://127.0.0.1:5000/menu">Меню</a>

        <h2>Реализованные роуты</h2>
        <ul>
            <li><a href="http://127.0.0.1:5000/lab1/oak">/lab1/oak - дуб</a></li>
            <li><a href="http://127.0.0.1:5000/lab1/student">/lab1/student - студент</a></li>
            <li><a href="http://127.0.0.1:5000/lab1/python">/lab1/python - python</a></li>
        </ul>

        <footer>
            &copy; Косарева Николета, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html> 
"""

@app.route("/menu")
def meenu():
    return"""
<!doctype html>
<html>
    <head>
        <title> Косарева Николета Вячеславовна, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа №1
        </header>

        <a href="http://127.0.0.1:5000/lab1">1. Первая лабораторная</a>
        

        <footer>
            &copy; Косарева Николета, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html> 
"""

@app.route('/lab1/oak')
def oak():
    return'''
<!doctype html>
<html>
    <body>
    <head>
        <link rel="stylesheet" type="text/css" href="'''+ url_for('static', filename='lab1.css')+'''">
    </head>
        <h1 class='dub'>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''">
    </body>
</html> 
'''

@app.route('/lab1/student')
def student():
    return'''
<!doctype html>
<html>
    <body>
        <h1>Косарева Николета Вячеславовна</h1>
        <img src="''' + url_for('static', filename='logo.png') + '''"
        style="width:20px, height:10px">
        
    </body>
</html> 
'''