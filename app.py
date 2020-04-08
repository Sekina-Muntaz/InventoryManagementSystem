# importing
from flask import Flask,render_template, request, redirect,url_for
import pygal

#instanciating a class
app=Flask(__name__)

# creating of endpoints
# 1. declaration of the route
# 2. A function embedded
# @app.route('/')
# def helloWorld():
#     return "<h1>Welcome to web development</h1>"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contacts():
    return render_template('contact.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/inventory',methods=['GET','POST'])
def inventory():

    # receive from a form
    if request.method=="POST":
        # print('worked')
        name=request.form['name']
        invType=request.form['invType']
        sellingPrice=request.form['sellingPrice']
        buyingPrice=request.form['buyingPrice']
        

        print(name)
        print(invType)
        print(sellingPrice)
        print(buyingPrice)
    
        return redirect(url_for('inventory'))


    return render_template('inventory.html')
@app.route('/addStock', methods=['GET','POST'])
def addStock():

    # # receive from a form
    if request.method=="POST":
        # print('worked')
        stock=request.form['stock']
        

        print(stock)
    
        return redirect(url_for('inventory'))


    return render_template('inventory.html')
@app.route('/addSale',methods=['POST','GET'])
def addSale():
    if request.method=="POST":
        sale=request.form['sale']
        

        print(sale)
       

        return redirect(url_for('inventory'))



    return render_template('inventory.html')
@app.route('/editInv', methods=['POST','GET'])
def editInv():
    if request.method=='POST':
        name=request.form['name']
        invType=request.form['invType']
        sellingPrice=request.form['sellingPrice']
        buyingPrice=request.form['buyingPrice']

        print(name)
        print(invType)
        print(sellingPrice)
        print(buyingPrice)

        return redirect(url_for('inventory'))
    
    
    
    return render_template('inventory.html')
@app.route('/data_visualization')
def data_visualization():
    # initializing pie chart
    pieChart=pygal.Pie()
    # add components to piechart
    pieChart.title="Corona Virus in Kenya"
    #  Partitioning your pie chart
    pieChart.add('Mombasa',60)
    pieChart.add('Nairobi',140)
    pieChart.add('Kilifi',100)
    pieChart.add('Kwale',50)
    pieChart.add('Mombasa',80)

    pieData=pieChart.render_data_uri()


    # line graph
    line_chart = pygal.Line()
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
    line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])

    lineData=line_chart.render_data_uri()

    

    return render_template('chart.html',pie=pieData,line=lineData)


    





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
    




