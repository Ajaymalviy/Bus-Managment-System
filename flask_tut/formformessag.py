from flask import Flask, render_template, request

app = Flask(__name__,template_folder="template")
@app.route('/')
def home():
    return render_template('exmp.html')

@app.route('/formlogin', methods=['POST'])
def login():
    if request.method=="POST":
     error = None
     name = request.args.get('name')
     password = request.args.get('pass')
     if name =="ajay" and password=="123":
         return "Successfully logged in"
     else:
         return "abort(407)"

if __name__ == "__main__":
    app.run(debug=True)
