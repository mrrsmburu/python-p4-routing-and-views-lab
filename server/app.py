#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '\n'.join(str(i) for i in range(parameter)) + '\n'
    return numbers

@app.route('/math/<path:num1>/<path:operation>/<path:num2>')
def math(num1, operation, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return 'Invalid numbers'

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Error: Division by zero'
    elif operation == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            return 'Error: Division by zero'
    else:
        return 'Invalid operation'
    
    if operation == 'div' or not result.is_integer():
        result = float(result)
    else:
        result = int(result)
    
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
