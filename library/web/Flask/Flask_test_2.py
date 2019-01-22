from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello Flask!!"

@app.route("/python")
def python():
    return "OPPython!!"

app.run()
