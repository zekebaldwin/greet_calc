from flask import flask
from operations import operations

app = Flask(__name__)

@app.route('/add')
def add_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)
    return str(result)

@app.route('/sub')
def sub_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = subtract(a, b)
    return str(result)

@app.route('/mult')
def mult_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = (a, b)
    return mult(result)

@app.route('/div')
def div_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)
    return str(result)




