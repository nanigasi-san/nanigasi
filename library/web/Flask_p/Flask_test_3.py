from flask import Flask,send_file
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello Flask!!"

@app.route("/img")
def img():
    return send_file("‪C:\\image\1.png",mimetype="image/png")

app.run()
