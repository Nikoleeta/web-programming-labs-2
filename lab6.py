from flask import Blueprint, render_template, request, make_response, redirect
from Db import db
from Db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user

lab6=Blueprint('lab6', __name__)

@lab6.route('/lab6')
def main():
    my_users=users.query.all()
    print(my_users)
    return 'result in console'

@lab6.route('/lab6/checkarticles')
def check():
    my_articles=articles.query.all()
    print(my_articles)
    return 'result in console'


@lab6.route('/lab6/register', methods=['GET', 'POST'])
def register():
    errors=''

    if request.method=='GET':
        return render_template('register.html')
    
    username_form=request.form.get('username')
    password_form=request.form.get('password')

    if username_form == '':
        errors='Пустое имя'
        return render_template('register.html', errors=errors)

    if len(password_form)<5:
        errors='Пароль меньше 5'
        return render_template('register.html', errors=errors)

    isUserExists=users.query.filter_by(username=username_form).first()

    if isUserExists is not None:
        errors='уже существует'
        return render_template('register.html', errors=errors)
    
    hashedPswd=generate_password_hash(password_form, method='pbkdf2')
    newUser=users(username=username_form, password=hashedPswd)

    db.session.add(newUser)
    db.session.commit()

    return redirect('/lab6/login')


@lab6.route('/lab6/login', methods=['GET', 'POST'])
def login():
    error=''
    if request.method=='GET':
        return render_template('login.html')
        
    username_form=request.form.get('username')
    password_form=request.form.get('password')

    if username_form=='' or password_form=='':
        error='не заполнены поля'
        return render_template('login.html', error=error)
    
    my_user=users.query.filter_by(username=username_form).first()
    

    if my_user is not None:
        if check_password_hash(my_user.password, password_form):
            login_user(my_user, remember=False)
            return redirect('/lab6/articles')
        else:
            error='неверный пароль'
            return render_template('login.html', error=error) 
    else:
        error='такого пользователя не существует'
        return render_template('login.html', error=error) 

@lab6.route('/lab6/articles')
@login_required
def articles_list():
    my_articles=articles.query.filter_by(user_id=current_user.id).all()
    return render_template('note2.html', articles=my_articles)