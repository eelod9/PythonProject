from flask import Flask
app = Flask(__name__)
import time
import random

#.venv\Scripts\Activate.ps1
#ran $env:FLASK_APP="hello.py" and then flask run
#turn on debug mode =>app.run(debug=True)

#Decorator example
#def decorator_function(function):
#    def wrapper_function():
#        function()
#    return wrapper_function
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function
def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

@delay_decorator 
def say_hello(): #when we call this, it will deplay by 2 sec cause of decorator
    print("Hello")





#Decorator giving additional functionality to an existing function
@app.route('/')
@make_bold
def hello_world():
    return '<h1 style="text-align:center"> Hello, Ella! </h1> \
            <h2>"Guess a number between 0 and 9 </h2>\
            <p><iframe src="https://giphy.com/embed/9dC7BpMHisDagbjgYq" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/corgi-lazy-hk-9dC7BpMHisDagbjgYq">via GIPHY</a></p>'


randomNum = random.randint(0,9)
@app.route('/<userInput>')
def result(userInput):
    uI = int(userInput)
    if uI<randomNum:
        return '<h1>Too low try again</h1> \
                <p><iframe src="https://giphy.com/embed/dIsQjjXQ1YAbjV2opK" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/lazy-corgi-dIsQjjXQ1YAbjV2opK">via GIPHY</a></p>'
    elif uI > randomNum:
        return '<h1>Too high try again</h1>\
                <p><iframe src="https://giphy.com/embed/KPVJXH61g2jHkdqZES" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/lazy-corgi-KPVJXH61g2jHkdqZES">via GIPHY</a></p>'
    else:
        return '<h1>Correct</h1>\
                <p><iframe src="https://giphy.com/embed/OSOOHw7N9gb3R06OU7" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/lazy-corgi-OSOOHw7N9gb3R06OU7">via GIPHY</a></p>'
    

@app.route('/bye')
def say_bye():
    return "Bye!"

@app.route('/username/<path:name>/<int:number>')
def greet(name,number):
    return f"Hello {name}, you are {number} years old"

if __name__ == "__main__":
    app.run(debug=True)