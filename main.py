
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/user-signup')
def usersignup():
    return render_template("user_sign_up.html", title='User Sign Up')

@app.route('/user-validate', methods=['POST'])
def user_validate():
    username = request.form['username']
    password = request.form['password']
    vpassword = request.form['vpassword']
    email = request.form['email']

    empty_field = True

    if username == '': 
        empty_field = True 
    elif password == '': 
        empty_field = True
    elif vpassword == '': 
        empty_field = True
    elif email == '': 
        empty_field = True
    else:
        empty_field = False

    if empty_field == True:
        return redirect('/user-signup')
    elif empty_field == False:
        return redirect('/user-confirmed')
    else:
        pass




@app.route('/user-confirmed', methods=['get'])
def user_confirmed():
    username = request.form['username']
    return render_template("user_confirmed.html", user=username)



app.run()