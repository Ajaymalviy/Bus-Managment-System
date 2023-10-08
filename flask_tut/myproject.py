from flask import Flask ,request,render_template
app=Flask(__name__,template_folder='template')
@app.route('/')
def first():
    return render_template('myproject.html')

@app.route('/', methods=['POST', 'GET']) 
def showdata():
    if request.method == 'POST':
        bus_id=request.form('bus_number')
        bus_number=request.form('bus_id')
        return render_template('dbms.html')
    else:
        return "Method not allowed"   
if __name__=="__main__":
    app.run(debug=True)