import mysql.connector
from flask import Flask, request, render_template

app = Flask(__name__,template_folder="templates")

# Database setup
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="myproject"
)
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS `users` (
                  id INT AUTO_INCREMENT PRIMARY KEY,
                  name VARCHAR(255),
                  password VARCHAR(255))''')
db.commit()

# Registration Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        # Check if the user already exists in the database
        cursor.execute("SELECT * FROM users WHERE name=%s", (name,))
        existing_user = cursor.fetchone()

        if existing_user:
            return 'User already exists. Please log in.'

        # If the user doesn't exist, add them to the database
        cursor.execute("INSERT INTO users (name, password) VALUES (%s, %s)", (name, password))
        db.commit()
    
        return 'Registration successful. You can now <a href="/login">log in</a>.', 201

    return render_template('register.html')

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        # Check if the user exists and the password matches
        cursor.execute("SELECT * FROM users WHERE name=%s AND password=%s", (name, password))
        user = cursor.fetchone()

        if user:
            return 'Login successful. Welcome, {}!'.format(name), 200
        else:
            return 'Invalid credentials. Please try again.', 401

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
