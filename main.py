from flask import request, make_response, redirect, render_template, session, url_for, flash
import unittest

from app import create_app
from app.firesotre_service import get_users, get_todos

app = create_app()

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response


@app.route('/hello')
def hello():
    user_ip = session.get('user_ip')
    user_name = session.get('username')

    context = {
        'user_ip': user_ip, 
        'user_name': user_name, 
        'todos': get_todos(user_name),
    }
    
    users = get_users()
    
    for user in users:
        print(user.id)
        print(user.to_dict()['password'])
    
    return render_template('hello.html', **context)