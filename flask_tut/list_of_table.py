from flask import Flask, render_template, request
import mysql.connector 

database_configuration = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'myproject'
}

app = Flask(__name__)

def connect_to_database():
    return mysql.connector.connect(**database_configuration)

@app.route("/")
def home():
    connection = connect_to_database() 
    cursor = connection.cursor()
    query = "SELECT * FROM conductor"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('list_of_table.html1', rows=rows)

if __name__== '__main__':
    app.run(debug=True)