
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/user-signup')
def usersignup():
    username = request.args.get('user')
    email = request.args.get('email')
    return render_template("user_sign_up.html", title='User Sign Up', username=username, email=email)

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
    
def is_empty(text):
    if text == '':
        return True 
    else:
        return False

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
    error = ''

    forms = (username, password, vpassword)

    if is_empty(username) or is_empty(password) or is_empty(vpassword):
        proceed = False
    else:
        if is_valid(username) and is_valid(password):
            if password_match(password, vpassword):
                if is_email(email):
                    proceed = True
                else:
                    proceed = False
            else:
                proceed = False
        else: 
            proceed = False



    if proceed == False:
        return redirect('/user-signup?user={0}&email={1}&error={2}'.format(username, email, error))
    else:
        return redirect('/user-confirmed?user={0}'.format(username))
        
        
@app.route('/re-user-signup')
def reusersignup():
    username = request.args.get('user')
    email = request.args.get('email')
    return render_template("user_sign_up.html", title='User Sign Up', username=username, email=email)

@app.route('/user-confirmed')
def user_confirmed():
    username = request.args.get('user') 
    return render_template("user_confirmed.html", user = username)
app.run()