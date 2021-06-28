from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'SECRET123'

todos = ['Todo 1', 'Todo 2', 'Todo 3']

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    # response.set_cookie('user_ip', user_ip)
    session['user_ip'] = user_ip

    return response


@app.route('/hello')
def hello_world():
    # user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    context = {
        'user_ip': user_ip, 
        'todos': todos
    }
    
    return render_template('hello.html', **context)