from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def calculator(a,b,operation):
    if(a.isnumeric() & b.isnumeric()):
        a = float(a)
        b = float(b)
        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'divide':
            result = a / b
        elif operation == 'multiply':
            result = a * b
        else:
            result = 'Operations supported are add, subtract, multiply, and divide.'
    else:
        result = 'Please enter a valid number.'
    return result