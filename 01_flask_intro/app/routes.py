from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kagan'}
    posts = [
        {
            'author': {'username': 'Ahmet'},
            'body': 'Beautiful day in Samsun!'
        },
        {
            'author': {'username': 'Hami'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/mylibrary')
def mylibrary():
    username = 'Ayşe'
    books = [
        {
            'title': 'Satranç',
            'author': 'Stefan Zweig',
            'is_read': True
        },
        {
            'title': 'Kızıl',
            'author': 'Stefan Zweig',
            'is_read': False
        },
        {
            'title': '1984',
            'author': 'George Orwell',
            'is_read': True
        },
        {
            'title': 'Korku',
            'author': 'Stefan Zweig',
            'is_read': False
        }
    ]
    return render_template(
        'mylibrary.html', title='My Library', username=username, books=books
    )
