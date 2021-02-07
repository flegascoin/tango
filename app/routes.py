from flask import render_template
from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for

# @app.route('/login')
# def login():
#     form = LoginForm()
#     return render_template('login.html', title='Login', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Fabrice'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Index', user=user, posts=posts)

@app.route('/logs')
def logs():
    user = {'username': 'Fabrice'}
    log_entries = [
        {
            'date': 'Monday, 01 February 2021',
            'event' : { 
                'location': 'Rochester, NY',
                'start_time': '09:30',
                'end_time': '10:30',
                'title': 'Meeting with Kodak folks.',
                'text': 'Lorem ipsum etc.'
                }
        },
        {
            'date': 'Monday, 01 February 2021',
            'event' : { 
                'location': 'unknown',
                'start_time': '12:30',
                'end_time': '14:00',
                'title': 'Lunch with Doug Bauer.',
                'text': 'Lorem ipsum etc.'
                }
        },
                {
            'date': 'Monday, 01 February 2021',
            'event' : { 
                'location': 'Bridgetown, NY',
                'start_time': '12:30',
                'end_time': '14:00',
                'title': 'Lunch with Doug Bauer',
                'text': 'Wondering what\'s the proper way to display HTML links within log entries like this one!'
                }
        }
    ]
    return render_template('logs.html', title='Log', user=user, log_entries=log_entries)