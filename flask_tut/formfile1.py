from flask import Flask, render_template, request

app = Flask(__name__, template_folder="template")

@app.route('/')
def upload():
    return render_template('form2.html')

@app.route('/success/', methods=['POST', 'GET'])  # It should be "methods" instead of "method"
def showdata():
    if request.method == 'POST':
        f= request.files('file')
        f.save('static'+f.filename)
        return "success"
    else:
        return "Method not allowed"

if __name__ == "__main__":
    app.run(debug=True)
