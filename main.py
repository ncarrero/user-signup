#need to make email optional and display username in welcome message

from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

def is_completed(text):
    try:
        text = not ''
        return True
    except ValueError:
        return False

@app.route("/", methods=['POST'])
def validate(): #pull out and validate data user input in the form
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify-password']
    email = request.form['email']

    username_error = '' #create empty string for variables
    password_error = ''
    verify_password_error = ''
    email_error = ''

    if not is_completed(username):
        username_error = 'Please enter a username.'
    elif len(username) < 3 or len(username) > 20 or ' ' in username:
        username_error = 'Username must contain no spaces and be between 3 and 20 characters long.'

    if not is_completed(password):
        password_error = 'Please enter a password.'
        password = ''
    elif len(password) < 3 or len(password) > 20 or ' ' in password:
        password_error = 'Username must contain no spaces and be between 3 and 20 characters long.'
        password = ''

    if not is_completed(verify_password):
        verify_password_error = 'Please enter your password again to verify.'
        verify_password = ''
    elif password != verify_password:
        verify_password_error = 'Password verification failed.  Please try again.'
        verify_password = ''

    if len(email) == 0:
        email = ''
    elif '@' not in email or '.' not in email or ' ' in email or len(email) < 3 or len(email) > 20:
        email_error = 'Email must contain 1 @ and . symbol, no spaces, and be between 3 and 20 characters long.'

    if not username_error and not password_error and not verify_password_error and not email_error:
        return render_template('welcome.html', username = username)
    else:
        return render_template('index.html', username=username,
        username_error = username_error, password = password, password_error = password_error,
        verify_password = verify_password, verify_password_error = verify_password_error, 
        email = email, email_error = email_error)

app.run()