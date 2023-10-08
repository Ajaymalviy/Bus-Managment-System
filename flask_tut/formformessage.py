# from flask import Flask,render_template,request
# import _mysql_connector
# database_configuration = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': 'password',
#     'database': 'sobham'
# }

 
# app =Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('formformessage.html')

# @app.route("/success", methods=['GET', 'POST'])# after fill the informn we want to change the directry
# def getting_data():
#     if request.method == 'POST':
#         name = request.form['name']
#         password=request.form['password']
#         # print(bus_model,'sdf')
#         try:
#             connection = mysql.connector.connect(**database_configuration)
#             cursor = connection.cursor()
#             # Execute a query to fetch details based on the entered bus_id
#             # with db.cursor() as cursor: 
#             cursor.execute(f'insert{name} into table ";')
#             result = cursor.fetchall()
#         except  :
            

            

            