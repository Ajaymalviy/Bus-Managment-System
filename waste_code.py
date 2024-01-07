
#----------------------------------login session -------------------------


# # Assuming 'app' is your Flask application instance
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'  # Specify the login view for redirecting unauthenticated users

# @login_manager.user_loader
# def load_user(user_id):
#     # Retrieve the user object from the database
#     cursor = db.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
#     user = cursor.fetchone()
#     cursor.close()
#     return User(user) if user else None

# # Your User class should inherit from UserMixin
# class User(UserMixin):
#     def __init__(self, user_data):
#         self.id = user_data['id']
#         self.username = user_data['name']
#         self.user_type = user_data['user_type']

# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('login'))





# ------------------------------------------- Login Required for Authentification -------------------------

# # the login_required function
# def login_required(view):
#     @wraps(view)
#     def wrapped_view(*args, **kwargs):
#         if 'username' in session:
#             # User is authenticated, execute the original view function
#             return view(*args, **kwargs)
#         else:
#             # User is not authenticated, redirect to the login page
#             flash("You are not logged in..! Login to perform action")
#             return redirect(url_for('signin'))

#     return wrapped_view

# @app.route('/logout')
# def logout():
#     # Clear the session to log the user out
#     session.pop('username', None)
#     # flash('You have been logged out.', 'info')
#     return render_template('index.html')



# -----------------------------this is our pages for auth----------------------require----------------

#----------------------------------login session -------------------------


# # Assuming 'app' is your Flask application instance
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'  # Specify the login view for redirecting unauthenticated users

# @login_manager.user_loader
# def load_user(user_id):
#     # Retrieve the user object from the database
#     cursor = db.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
#     user = cursor.fetchone()
#     cursor.close()
#     return User(user) if user else None

# # Your User class should inherit from UserMixin
# class User(UserMixin):
#     def __init__(self, user_data):
#         self.id = user_data['id']
#         self.username = user_data['name']
#         self.user_type = user_data['user_type']

# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('login'))

