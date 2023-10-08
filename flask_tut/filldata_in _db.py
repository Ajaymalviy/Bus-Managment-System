from flask import Flask,request,jsonify ,render_template
import mysql.connector
app=Flask(__name__,template_folder='templates')
@app.route('/')
def first():
    return render_template("myproject.html")

def variable_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='myproject'
    )
@app.route('/success',methods=['GET','POST'])
def add_item():
    if request.method == 'POST':
        #bus_id = request.args.get('bus_id')
        driver_id = request.args.get('driver_id')
        conductor_id = request.args.get('conductor_id')
        bus_number = request.args.get('bus_number')
        bus_model = request.args.get('bus_model')
        seating_capacity = request.args.get('seating_capaciy')
        route = request.args.get('route')
        departure_time= request.args.get('departure_time')
        arrival_time= request.args.get('arrival_time')
    
    conn = variable_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO bus_detail(driver_id,conductor_id,bus_number,bus_model,seating_capacity,route,departure_time,arrival_time) values(%s, %s, %s, %s, %s, %s, %s, %s)',(driver_id,conductor_id,bus_number,bus_model,seating_capacity,route,departure_time,arrival_time))
    conn.commit()
    conn.close()
    return "sucesss"

if __name__ == '__main__':
    app.run(debug=True)
