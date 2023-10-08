from flask import Flask, render_template, request

app = Flask(__name__, template_folder="template")

@app.route('/')
def registration():
    return render_template('form.html')

@app.route('/success/', methods=['POST', 'GET'])  # It should be "methods" instead of "method"
def showdata():
    if request.method == 'POST':
        result = request.form
        return render_template('result.html', result=result)
    else:
        return "Method not allowed"

if __name__ == "__main__":
    app.run(debug=True)
