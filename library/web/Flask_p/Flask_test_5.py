from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")#Hello
def hello():
    return "Hello Flask!!"

@app.route("/python")
def python():
    return render_template("Flask_test_5_python.html")

app.run()
