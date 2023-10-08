from flask import Flask, render_template, request,session,redirect

app = Flask(__name__,template_folder="template")
# app.secret_key='login'

# @app.route('/')
# def login1():
#     return render_template('session1.html')
# @app.route('/logout')
# def logout():
#     return render_template('session1.html')

# @app.route('/login', methods=['POST'])
# def login():
#     if request.method=='POST':
#         username=request.form('username')
#         password=request.form('password')
#     if (username=='ajay' and password=='143'):
#         session['email']=username
#         return render_template(email=username)
#     else:
#         msg='invalid username/password'
#         return render_template( 'session1.html',msg=msg)
# @app.route('/profile')
# def profile():
#     if email in session:
#         email=session['email']
#         return render_template('profile.html',name=email)
#     else:
#         msg='login_first'
#         return render_template('session1.html',msg= name)
#LOGIN LOG OUT
@app.route('/login', methods=['POST'])
def login():
    user = get_user(request.form['username'])

    if user.check_password(request.form['password']):
        login_user(user)
        app.logger.info('%s logged in successfully', user.username)
        return redirect(url_for('login'))
    else:
        app.logger.info('%s failed to log in', user.username)
        #abort(401)  or print invalid 