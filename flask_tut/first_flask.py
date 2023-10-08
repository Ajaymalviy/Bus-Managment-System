from flask import Flask
app=Flask(__name__)  #this is the object creation of class Flask
#now we have to declear route
@app.route('/')
def hello():
    return "hellw --yr"
@app.route('/ajay/')
def name():
    return "this ajay bytheway dont get confused ,just carry on buddy ,i manage"  
app.run(debug=True) #if our program are not changing there port show message for changing the port or different server then run the comand on terminal
#netstat -tuln | grep 5000
#app.route (debag=True) then it actually wants to prove that our debag is active or on now we does not want to do same 
#thing again and again
# if i want to change the host or post name we done that also as like
#app.route(host="0.0.0",post=" ",debug=True)




