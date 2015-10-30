__author__ = 'MengdanZhang'
import os
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world!"

app.run()

# --#