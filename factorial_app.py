from flask import Flask
import math
app = Flask(__name__)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

@app.route("/<n>")
def hello(n):
    return str(factorial(int(n)))


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
