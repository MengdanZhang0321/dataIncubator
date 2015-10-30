__author__ = 'MengdanZhang'
from flask import Flask
app = Flask("hello")

@app.route("/")
def hello():
    return "Hello world!"

app.run()

# --#