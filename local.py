from flask import Flask

myapp = Flask(__name__)

@myapp.route('/')
def index():
    return "Hello.\nIt is nanigasi wab."
