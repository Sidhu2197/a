from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>hi mowa -:)</h1>"


@app.route("/hello")
def hello():
    return "hello world"


@app.route("/greet/<name>")
def greet(name):
    return f"hello{name}"


@app.route("/add/<number1>/<number2>")
def add(number1, number2):
    return f"{number1} + {number2} = {number1 + number2}"


@app.route("/handle_url_params")
def handle_params():
    if "greeting" in request.args.keys() and "name" in request.args.keys():
        greeting = request.args.get("greeting")
        name = request.args.get("name")
        return f"{greeting},{name}"
    else:
        return "some parameters are missing"


app.run(host="127.0.0.1", port=5055, debug=True)
