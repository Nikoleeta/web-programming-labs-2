from flask import Flask, redirect
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