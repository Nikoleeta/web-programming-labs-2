from flask import Blueprint, redirect, url_for
lab1=Blueprint('lab1',__name__)

@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect ("/menu", code=302)


@lab1.route("/lab1")
def lab():
    return"""
<!doctype html>
<html>
    <head>
        <title> Косарева Николета Вячеславовна, лабораторная 1</title>
    </head>
    <body>
        <link rel="stylesheet" type="text/css" href="'''+ url_for('static', filename='lab1.css')+'''">
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
            <li><a href="http://127.0.0.1:5000/lab1/bi">/lab1/bi - бизнес-информатика</a></li>
        </ul>

        <footer>
            &copy; Косарева Николета, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html> 
"""


@lab1.route("/menu")
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

        <a href="/lab1">1. Первая лабораторная</a>
        <p><a href="/lab2">2. Вторая лабораторная</a></p>
        <p><a href="/lab3/">3. Третья лабораторная</a></p>
        <p><a href="/lab4/">4. Четвертая лабораторная</a></p>
        <p><a href="/lab5/">5. Пятая лабораторная</a></p>
        <p><a href="/lab6">6. Шестая лабораторная</a></p>
        <p><a href="/lab7">7. Седьмая лабораторная</a></p>
        <footer>
            &copy; Косарева Николета, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html> 
"""


@lab1.route('/lab1/oak')
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


@lab1.route('/lab1/student')
def student():
    return'''
<!doctype html>
<html>
    <body>
    <head>
        <link rel="stylesheet" type="text/css" href="'''+ url_for('static', filename='lab1.css')+'''">
    </head>
        <img class='img2' src="''' + url_for('static', filename='logo.png') + '''">
        <h1>Косарева Николета Вячеславовна</h1>
    </body>
</html> 
'''


@lab1.route('/lab1/python')
def python():
    return'''
<!doctype html>
<html>
    <body>
    <head>
        <link rel="stylesheet" type="text/css" href="'''+ url_for('static', filename='lab1.css')+'''">
    </head>
        <h1 class="text">Applications for Python</h1>
        <p>Python is used in many application domains. Here's a sampling.</p>
        <li>The Python Package Index lists 
        thousands of third party modules for Python.</li>
        
        <h2 class="text">Web and Internet Development</h2>
        <p>Python offers many choices for web development:</p>
        <li>Frameworks such as Django and Pyramid.</li>
        <li>Micro-frameworks such as Flask and Bottle.</li>
        <li>Advanced content management systems such as Plone and django CMS.</li>
    
        <p>Python's standard library supports many Internet protocols:</p>
        <li>HTML and XML</li>
        <li>JSON</li>
        <li>E-mail processing.</li>
        <li>Support for FTP, IMAP, and other Internet protocols.</li>
        <li>Easy-to-use socket interface.</li>

        <img class='img3' src="''' + url_for('static', filename='python.jpg') + '''">
    </body>
</html> 
'''


@lab1.route('/lab1/bi')
def bi():
    return'''
<!doctype html>
<html>
    <body>
    <head>
        <link rel="stylesheet" type="text/css" href="'''+ url_for('static', filename='lab1.css')+'''">
    </head>
    <div class='teext2'><img class='img4' src="''' + url_for('static', filename='8.png') + '''">
    Бизнес-информатика</div>
    
    <h1 class='teext'>ЧЕМ УНИКАЛЬНА БИЗНЕС-ИНФОРМАТИКА?</h1>

    <p><h2 class='teext2'>Формирование компетенций</h2></p>
    <p>Возможность выйти на экспертный уровень в 
    использовании методов и инструментов Data Science,
    позволяющих решать задачи на стыке предметных областей и 
    передовых компьютерных технологий</p>

    <p><h2 class='teext2'>Проектный опыт</h2></p>
    <p>Большой объём внеаудиторной деятельности,, предусматривающей 
    включение студента в практическую работу как в университете, так и за его пределами.
    Это является хорошим шансом установить контакт с будущим работодателем :)</p>

    <p><h2 class='teext2'>Яркая студенческая жизнь</h2></p>
    <p><p>Большой объём внеаудиторной деятельности,, предусматривающей 
    включение студента в практическую работу как в университете, 
    так и за его пределами. Это является хорошим шансом установить 
    контакт с будущим работодателем :)</p></p>

    </body>
</html> 
'''
