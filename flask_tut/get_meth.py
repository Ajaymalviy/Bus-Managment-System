from flask import Flask, render_template
import mysql.connector
app = Flask(__name__, template_folder="templates")
app.config['DB_HOST'] = 'localhost'
app.config['DB_USER'] = 'root'
app.config['DB_PASSWORD'] = 'password'
app.config['DB_DATABASE'] = 'myproject'

def connect_to_database():
    return mysql.connector.connect(
        host=app.config['DB_HOST'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        database=app.config['DB_DATABASE']
    )
@app.route('/')
def retrieve_data():
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "SELECT * FROM driver"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('data.html', rows=rows)
if __name__ == '__main__':
  app.run(debug=True)
