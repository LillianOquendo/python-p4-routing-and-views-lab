#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

#@app.route is a decorator. It specifies that the index() should handle the request
#to the base url to add a '/' and then the <h1> element

@app.route ('/')
def index ():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

#This second @app.route is going to take a string as a parameter in the terminal and to the browser

@app.route( '/print/<string>' )
def print_string( string ):
    print( string )
    return f'{ string }'

@app.route( '/count/<int:number>' )
def count( number ):
    result = f""
    for n in range( number ):
        result += f"{ n }\n"
    return result

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1:int, operation:str, num2:int):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)




if __name__ == '__main__':
    app.run(port=5555, debug=True)