#script for adding  the button url of particular form or particular bus details before and after.

@app.route("/show") #our first directry which is open
def index():
    return render_template("partifular_bus.html")#it will though us to the html page which is open at first

@app.route("/success", methods=['GET', 'POST'])
def getting_data():
    if request.method == 'POST':
        bus_id = request.form['bus_id']
        driver_id = request.form['bus_id']
        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            cursor.execute(f'SELECT seating_capacity,route,departure_time,arrival_time, FROM bus_detail WHERE bus_id ="{bus_id}";')
            result = cursor.fetchall()
            cursor.close()
            cursor = connection.cursor()
            cursor.execute(f'SELECT source,destination,departuare_time,arrival_time FROM ticket WHERE bus_id = "{_id}";')
            result2 = cursor.fetchall()

        except mysql.connector.Error as e:
            result = e
            result2 = e #we can do same as the above one where both result being same as e,and except it
        
        finally:
            cursor.close()
            connection.close()

    return render_template('particular_form.html', result=result, result2=result2)
