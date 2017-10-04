
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/user-signup')
def usersignup():
    username = request.args.get('user')
    email = request.args.get('email')
    error = request.args.get('error')
    username_error = request.args.get('username_error')
    password_error = request.args.get('password_error')
    vpassword_error = request.args.get('vpassword_error')
    email_error = request.args.get('email_error')
    
    return render_template("user_sign_up.html", title='User Sign Up', username=username, email=email,username_error=username_error, password_error=password_error, vpassword_error=vpassword_error, email_error=email_error)

def is_valid(text):
    error = ''
    if len(text) >= 3 and len(text) <= 20:
        for char in text:
            if char == "":
                error = 'should contain no space.'
                break
                return False
            else:
                return True
    else:
        error = 'is not correct length.'
        return False
    
def not_empty(text):
    if text == '':
        return False
    else:
        return True

def password_match(text, text2):
    error = ''
    if text == text2:
        return True
    else:
        error = 'Passwords do not match.'
        return False

def is_email(text):
    if text != '':
        error = ''
        if is_valid(text):
            email = ''
            for char in text:
                if char == '@':
                    email += '@'
                else:
                    pass
                if char == '.':
                    email += '.'
                else:
                    pass
            if email == '@.':
                return True
            else:
                error = ' is not a valid email.'
                return False

        else:
            return False    
    else: 
        return True


@app.route('/user-validate', methods=['POST'])
def user_validate():
    username = request.form['username']
    password = request.form['password']
    vpassword = request.form['vpassword']
    email = request.form['email']
    proceed = False
    username_error = ''
    password_error = ''
    vpassword_error = ''
    email_error = ''

    if not_empty(username):
        if not_empty(password):
            if not_empty(vpassword):
                if is_valid(username):
                    if is_valid(password):
                        if password_match(password, vpassword):
                            if is_email(email):
                                return redirect('/user-confirmed?user={0}'.format(username))
                            else:
                                email_error = 'Not a valid email'
                                return redirect('/user-signup?user={0}&email={1}&username_error={2}&password_error={3}&vpassword_error={4}&email_error={5}'.format(username, email, username_error, password_error, vpassword_error, email_error))

                        else:
                            password_error = 'Passwords do not match.'
                            return redirect('/user-signup?user={0}&email={1}&username_error={2}&password_error={3}&vpassword_error={4}&email_error={5}'.format(username, email, username_error, password_error, vpassword_error, email_error))
                    else:
                        password_error = 'Password not valid'
                        return redirect('/user-signup?user={0}&email={1}&username_error={2}&password_error={3}&vpassword_error={4}&email_error={5}'.format(username, email, username_error, password_error, vpassword_error, email_error))
                else:
                    username_error = 'Username not valid.'
                    return redirect('/user-signup?user={0}&email={1}&username_error={2}&password_error={3}&vpassword_error={4}&email_error={5}'.format(username, email, username_error, password_error, vpassword_error, email_error))
            else:
                vpassword_error = 'Password empty'
                return redirect('/user-signup?user={0}&email={1}&username_error={2}&password_error={3}&vpassword_error={4}&email_error={5}'.format(username, email, username_error, password_error, vpassword_error, email_error))
        else:
            password_error = 'Password empty'
            return redirect('/user-signup?user={0}&email={1}&username_error={2}&password_error={3}&vpassword_error={4}&email_error={5}'.format(username, email, username_error, password_error, vpassword_error, email_error))
    else:
        username_error = 'Username empty.'
        return redirect('/user-signup?user={0}&email={1}&username_error={2}&password_error={3}&vpassword_error={4}&email_error={5}'.format(username, email, username_error, password_error, vpassword_error, email_error))
        
@app.route('/user-confirmed')
def user_confirmed():
    username = request.args.get('user') 
    return render_template("user_confirmed.html", user = username)
app.run()