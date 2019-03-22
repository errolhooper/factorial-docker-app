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
    response = {
    "input": 0,
    "output": 0
    }

    fact_output = str(factorial(int(n)))
    response["input"] = n
    response["output"] = fact_output 

    # convert into JSON:
    json_response = json.dumps(response)

    # the result is a JSON string:
    return json_response


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
