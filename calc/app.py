from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route("/add")
def addition():
    try:
        a = int(request.args["a"])
        b = int(request.args["b"])
        return str(add(a, b))
    except:
        return "Bad input parameters"

@app.route("/sub")
def subtraction():
    try:
        a = int(request.args["a"])
        b = int(request.args["b"])
        return str(sub(a, b))
    except:
        return "Bad input parameters"

@app.route("/mult")
def multiplication():
    try:
        a = int(request.args["a"])
        b = int(request.args["b"])
        return str(mult(a, b))
    except:
        return "Bad input parameters"

@app.route("/div")
def division():
    try:
        a = int(request.args["a"])
        b = int(request.args["b"])
        return str(div(a, b))
    except:
        return "Bad input parameters"

@app.route("/math/<operation>")
def math(operation):
    try:
        operations = {"add": add, "sub": sub, "mult": mult, "div": div}
        a = int(request.args["a"])
        b = int(request.args["b"])
        return str(operations[operation](a, b))
    except:
        return "Bad input parameters"