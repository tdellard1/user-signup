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
    if len(text) >= 3 and len(text) <= 20:
        for char in text:
            if char == "":
                return  "Field should't contain no space."
            else:
                return ''
    else:
        return "Field isn't correct length."
    
def not_empty(text):
    if text == '':
        return 'Field is empty'
    else:
        return ''

def password_match(text, text2):
    
    if text == text2:
        return ''
    else:
        return 'Fields do not match.'

def is_email(text):
    if text != '':
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
        if '@' in email and '.' in email:
            return ''
        else:
            return 'Field is not valid'
            
    else: 
        return ''


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

    username_error = not_empty(username)
    password_error = password_match(password, vpassword)
    username_error = is_valid(username)
    password_error = not_empty(password)
    password_error = is_valid(password)
    vpassword_error = not_empty(vpassword)
    vpassword_error = is_valid(vpassword)
    email_error = is_valid(email)
    email_error = is_email(email)

    if not username_error and not password_error and not vpassword_error and not email_error:
        return redirect('/user-confirmed?user={0}'.format(username))
    else:
        return redirect('/user-signup?user={0}&email={1}&username_error={2}&password_error={3}&vpassword_error={4}&email_error={5}'.format(username, email, username_error, password_error, vpassword_error, email_error))
              
@app.route('/user-confirmed')
def user_confirmed():
    username = request.args.get('user') 
    return render_template("user_confirmed.html", user = username)
app.run()