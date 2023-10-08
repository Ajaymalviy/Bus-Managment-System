from flask import Flask
app=Flask(__name__)
@app.route('/')
def good():
    return "what is your birth date"
    #return "what is your name"
# @app.route('/anything')
# def change():
#     return "just whatewere you want"
# app.run(debug=True)
# @app.route('/<name>')
# def newthing(name):
#     return "ohh that's gud name "+name
app.route('/<int>/')
def birth(date):
    return " your date is:" % date
app.run(debug=True)
