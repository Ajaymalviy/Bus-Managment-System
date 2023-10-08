from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
import bcrypt

app = Flask(__name__,template_folder='templates')

app.secret_key = 'secrets.token_hex(16)'  # Replace with a secret key for sessions

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "password",
    "database": "myproject",
}

db = mysql.connector.connect(**db_config)

# Create a cursor to execute SQL queries
cursor = db.cursor()

# Create a table for user registration if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    mobile_number VARCHAR(20) NOT NULL,
    city VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    user_type VARCHAR(50) NOT NULL
)
"""
cursor.execute(create_table_query)
db.commit()


# create_table_query_bus_pass="""
# CREATE TABLE bus_pass (
#     pass_id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255) NOT NULL,
#     phone VARCHAR(15) NOT NULL,
#     address TEXT NOT NULL,
#     age INT NOT NULL,
#     user_type VARCHAR(10) NOT NULL,
#     aadhaar VARCHAR(12) NOT NULL
# );
# """
# cursor.execute(create_table_query_bus_pass)
# db.commit()


@app.route('/')
def home():
    return render_template('login_web.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = db.cursor()

        # Fetch user data based on the provided username
        cursor.execute("SELECT name, password FROM users WHERE name=%s", (username,))
        user_data = cursor.fetchone()
        
        cursor.close()

        if user_data:
            stored_password = user_data[1]
            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                # Passwords match, you can log in
                # Add your login logic here
                return render_template('buttons.html')
            else:
                return "Incorrect password. Please try again."
        else:
            return "Username not found. Please register."

    return render_template('login_web.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        mobile_number = request.form['mobile_number']
        city = request.form['city']
        email = request.form['email']
        user_type = request.form['user_type']

        # Check if both username and password already exist
        cursor.execute("SELECT name, password FROM users WHERE name=%s", (username,))
        user_data = cursor.fetchone()

        if user_data:
            stored_password = user_data[1].encode('utf-8')
            if bcrypt.checkpw(password.encode('utf-8'), stored_password):
                return "Username and password already exist. You can log in now."

        # Commit any pending changes from previous queries
        db.commit()

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Insert the new user into the database
        insert_query = "INSERT INTO users (name, password, mobile_number, city, email, user_type) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (username, hashed_password, mobile_number, city, email, user_type))

        # Commit the transaction after the INSERT query
        db.commit()

        return redirect(url_for('login'))

    return render_template('registration_page.html')

@app.route('/bus_details',methods=['GET'])
def bus_details():
    try:
        cursor = db.cursor(dictionary=True)
        query = "SELECT * FROM bus_detail LIMIT 140"  # Modify this query based on your table structure
        cursor.execute(query)
        bus_data = cursor.fetchall()
        cursor.close()
        return render_template('bus_details.html', bus_data=bus_data)
    except Exception as e:
        print(e)
        flash("An error occurred while fetching bus details.", "error")
        return redirect(url_for('bus_details'))

@app.route('/delete_bus', methods=['POST'])
def delete_bus():
    try:
        bus_id = int(request.form.get('bus_id'))
        
        # Delete the bus record from the database
        cursor = db.cursor()
        query = "DELETE FROM bus_detail WHERE bus_id = %s"
        cursor.execute(query, (bus_id,))
        db.commit()
        cursor.close()
        
        flash("Bus deleted successfully.", "success")
        return redirect(url_for('bus_details'))
    except Exception as e:
        db.rollback()
        flash(f"An error occurred while deleting the bus.:{e}", "error")
        return redirect(url_for('bus_details'))
    
    


# Create a new route for platform details
@app.route('/platform_details')
def platform_details():
    # Query for my database to fetch platform details
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM platform LIMIT 70"  
    cursor.execute(query)
    platform_data = cursor.fetchall()
    cursor.close()

    return render_template('platform.html', platform_data=platform_data)


# Create a new route for ticket routes
@app.route('/ticket_routes')
def ticket_routes():
    # Query your database to fetch ticket routes
    cursor = db.cursor(dictionary=True)
    query = "SELECT route FROM bus_detail LIMIT 30"  # Adjust the query as needed
    cursor.execute(query)
    ticket_data = cursor.fetchall()
    cursor.close()

    return render_template('ticket.html', ticket_data=ticket_data)



@app.route("/show") #our first directry which is open
def index():
    return render_template("particular_bus.html")#it will though us to the html page which is open at first

@app.route("/success", methods=['GET', 'POST'])
def getting_data():
    result = []

    if request.method == 'POST':
        bus_id = request.form['bus_id']
        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            cursor.execute(f'SELECT bus_model,seating_capacity, route, departure_time, arrival_time FROM bus_detail WHERE bus_id = "{bus_id}";')
            result = cursor.fetchall()

        except mysql.connector.Error as e:
            # Handle the error as needed
            print(f"Error: {e}")

        finally:
            cursor.close()
            connection.close()
            

    return render_template('particular_form.html', result=result)

#this is only for opening html file
@app.route('/mission')
def mission():
    # Your mission view logic here
    return render_template('mission.html')




@app.route('/service')
def service():
    # Your services view logic here
    return render_template('service.html')




@app.route('/transport')
def transport():
    # Your referemces view logic here
    return render_template('transport_of_goods.html')




@app.route('/bus_history')
def bus_history():
    # Your bus_history view logic here
    return render_template('bus_history.html')




@app.route('/about_us')
def about_us():
    # Your about_us view logic here
    return render_template('about_us.html')



@app.route('/our_team')
def our_team():
    # Your our_team view logic here
    return render_template('our_team.html')



@app.route('/contact')
def contact():
    # Your contact view logic here
    return render_template('contact.html')


@app.route('/bus_pass',methods = ['GET'])
def bus_pass():
    # Your bus-pass view logic here
    return render_template('bus_pass.html')


@app.route('/services', methods=['POST'])
def services():
    if request.method == 'POST':
        # Get data from the form
        name = request.form['name']
        phone = request.form['phone']
        address = request.form['address']
        age = request.form['age']
        user_type = request.form['userType']
        aadhaar = request.form['aadhaar']

        try:
            cursor = db.cursor()
            insert_query = "INSERT INTO bus_pass (name, phone, address, age, user_type, aadhaar) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (name, phone, address, age, user_type, aadhaar))
            db.commit()
            cursor.close()
            return "Data inserted successfully."
        except mysql.connector.Error as e:
            return f"An error occurred while inserting data: {str(e)}"
        finally:
            if cursor:
                cursor.close()

    return render_template('bus_pass.html')



@app.route('/driver_manipulate')
def driver_manipulate():
    # Your driver manipulation on database view logic here
    return render_template('what_in_driver.html')


@app.route('/conductor_manipulate')
def conductor_manipulate():
    # Your conductor manipulation view logic here
    return render_template('what_in_conductor.html')



@app.route('/platform_manipulate')
def platform_manipulate():
    # Your platform manipulation view logic here
    return render_template('what_in_platform.html')




@app.route('/route_manipulate')
def route_manipulate():
    # Your route manipulation view logic here
    return render_template('what_in_route.html')




@app.route('/passenger_manipute')
def passenger_manipulate():
    # Your contact view logic here
    return render_template('what_in_passenger.html')


@app.route('/bus_manipulate')
def bus_manipulate():
    # Your bus manipulation view logic here
    return render_template('what_change.html')


@app.route('/manipulationall')
def manipulationall():
    # Your first of manuplation  view logic here
    return render_template('manipulationall.html')




if __name__ == '__main__':
    app.run(debug=True)
