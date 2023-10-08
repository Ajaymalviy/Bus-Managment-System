#always create html file in template in static we use the visible web things but in template we use for hidding
from flask import Flask,render_template
app=Flask(__name__)  #this is the object creation of class Flask
#now we have to declear route
@app.route('/')
def hello():
    return "<html> <body> <h1>this is html first prog</h1> </body> </html>"
    return render_template('index.html')
app.run(debug=True)