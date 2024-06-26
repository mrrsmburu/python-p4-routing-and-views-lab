#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views<h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return f'<h2>{parameter}</h2>'

@app.route('/count/<int:parameter>')
def count(parameter):
    count_list = '<br>'.join(str(i) for i in range(parameter + 1))
    return f'<h2>Counting up to {parameter}:</h2><p>{count_list}</p>'

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2 if num2 != 0 else 'undefined (division by zero)'
    elif operation == '%':
        result = num1 % num2
    else:
        result = 'Invalid operation'
    return f'<h2>{num1} {operation} {num2} = {result}</h2>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
