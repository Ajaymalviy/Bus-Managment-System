# appofproject.py
from flask import Flask, render_template, request
import mysql.connector #for connect with mysql
#from config_last import DATABASE_CONFIG,can also be done with the another file where our data are feed

db_config = {
    'host':'localhost',
    'user':'root',
    'password':'password',
    'database':'myproject'
}
app = Flask(__name__)

@app.route("/") #our first directry which is open
def index():
    return render_template("app_lastform.html")#it will though us to the html page which is open at first

@app.route("/success", methods=['GET', 'POST'])# after fill the informn we want to change the directry
def getting_data():
    if request.method == 'POST':
        bus_model = request.form['bus_model']
        driver_id=request.form['driver_id']
        # print(bus_model,'sdf')
        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            # Execute a query to fetch details based on the entered bus_id
            # with db.cursor() as cursor:
            cursor.execute(f'SELECT bus_number FROM bus_detail WHERE bus_model like "{bus_model}";')
            cursor.execute(f'SELECT first_name FROM driver where driver_id ="{driver_id}";')
            result = cursor.fetchall()
            result2 = cursor.fetchall()

            # print(result)
            #print(result2)

        except mysql.connector.Error as e:
            result = e
            result2 = e
        
        finally:
    
            cursor.close()
            connection.close()

    return render_template('null.html', result=result,result2=result2)
    


