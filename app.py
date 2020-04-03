# importing
from flask import Flask

#instanciating a class
app=Flask(__name__)

# creating of endpoints
# 1. declaration of the route
# 2. A function embedded
@app.route('/')
def helloWorld():
    return "<h1>Welcome to web development</h1>"

@app.route('/home')
def home():
    return "<h1>Welcome Home</h1>"

@app.route('/about')
def about():
    return "<h1>Welcome to the about page</h1>"

@app.route('/contact_us')
def contactUs():
    return "<h1>Welcome to the contact us page</h1>"

@app.route('/services')
def services():
    return "<h1>Welcome to the  services page</h1>"

@app.route('/name/<name>')
def my_name(name):
    return f"<h1>My name is {name}</h1>"

# @app.route('/sum/<num1,num2>')
# def getSum(num1,num2):
#     sum=num1+num2
#     return sum

# adding two numbers dynamically,
# cant return an in to a route
@app.route('/sum/<num1>/<num2>')
def getSum(num1,num2):
    sum=int(num1)+int(num2)
    return str(sum)

@app.route('/division/<num1>/<num2>')
def div(num1,num2):
    res=int(num1)/int(num2)
    return str(res)

@app.route('/multiplication/<num1>/<num2>')
def multiply(num1,num2):
    res=int(num1)*int(num2)
    return str(res)
    
@app.route('/my_story/<name>/<age>/<town>')
def myStory(name,age,town):
    return f"<h1>My name is {name}, I am {age} years old, I come from {town} town</h1>"

    
    

if __name__=="__main__":
    app.run()
    




