from flask import Flask, render_template, request, redirect, url_for, send_file
import mysql.connector

# Define your MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password'
}

app = Flask(__name__)

#--------------------------------------------------------------------

#  function for creating a table
def create_table(column_detail, table_name):

    # splitting value by ","   
    str1 = column_detail.split(",")
    

    str2 = []
    
    # splitting value by ":" and storing in str2
    for i in str1:
        s = i.split(":")
        str2.append(s)
    
    # query 
    query = f"create table {table_name} ("
       
    # traversing into list  
    for i in str2:

        #  traversing inner list
        for j in i:
            query += f" {j}"
        if i != str2[-1]:
            query += " , "
    
    # ending part of query
    query += ");"

    # returning the query
    return query
#_---------------------------------------------------------------------

#  function to generate schema and for download that
def generate_schema_sql(db_name):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Select the database
        cursor.execute(f"USE {db_name}")

        # Get the list of tables in the database
        cursor.execute("SHOW TABLES")
        tables = [x[0] for x in cursor.fetchall()]


        schema_sql = ''' '''
        for table_name in tables:


            # print(table_name)
            cursor.execute(f"SHOW CREATE TABLE {table_name}")
            create_query = cursor.fetchone()[1]
            # print(create_query)

            schema_sql += f"\n\n-- Table: {table_name}\n"
            schema_sql += f"{create_query}\n;"

    except mysql.connector.Error as err:
        return f"Error: {err}"

    finally:
        cursor.close()
        connection.close()

    return schema_sql

#----------------------------------------------------------------------------



@app.route('/')
def index():
    return render_template('index.html')

# this function will be triggered by index.html
@app.route('/create_tables/', methods=['POST'])
def create_tables():
    global db_name 
    db_name  = request.form['dbName']
    num_tables = int(request.form['numTables'])
    return render_template('table.html', db_name=db_name, num_tables=num_tables)



@app.route('/submit_table_details/<db_name>/<int:num_tables>/', methods=['POST'])
def table_details(db_name, num_tables):
          
    table_name_list = request.form.getlist('tableName')
    column_details_list = request.form.getlist('columnDetails')

    messages = []

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Create database if not exists
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    cursor.execute(f"USE {db_name}")


    # Iterate through the provided table names and column details
    num = 1
    for table_name, column_details in zip(table_name_list, column_details_list):
        create_query = create_table(column_details, table_name)
        print(create_query)

        try:
            # Execute the create table query
            cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
            cursor.execute(create_query)
            connection.commit()
            messages.append( (f'Table {num}', table_name, 'Table created successfully') )
            num += 1
        except mysql.connector.Error as err:
            messages.append( (f'Table {num}', table_name, err) )
            num += 1
    
    cursor.close()
    connection.close()

    total = 0
    for i in messages:
        if i[2]=='Table created successfully':
            total += 1

    return render_template('output.html', messages=messages, total= total, num_tables=num_tables, db_name=db_name )


#  to download the schema file
@app.route("/download_schema/<db_name>", methods=['GET','POST'])
def download_schema(db_name):

    if request.method == 'POST':

        schema_sql = generate_schema_sql(db_name)

        print(schema_sql)

        # Save the SQL to a file
        file_path = f"{db_name}_schema.sql"
        with open(file_path, 'w') as file:
            file.write(schema_sql)

        # Provide the file for download
        return send_file(file_path, as_attachment=True) # If set to True, the file will be sent as an attachment








if __name__ == '__main__':
    app.run(debug=True)