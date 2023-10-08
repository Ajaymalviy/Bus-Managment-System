from flask import Flask,redirect,url_for
objec=Flask(__name__)
@objec.route('/')
def student():
    return "i am student"#i gave it bydefault
@objec.route('/faculty')
def faculty():
    return "i am faculty"# i declear it byself
@objec.route('/user/<name>')#i wrote that for rearranging the name modal
def user(name):
    if name==student:
       return redirect(url_for('student'))
    if name==faculty:
        return redirect(url_for('faculty'))
objec.run(debug=True)