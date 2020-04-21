# importing
from flask import Flask,render_template, request, redirect,url_for
import pygal
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from config.config import Development,Production

'''
two ways of connecting to db in flask
1. psycopg2-use sql statement
2. flask sql alchemy- use orm(object relational mapper)

psycopg2 is a python library
HOW TO USE IT
1. install it
2. set it up
-username
-pwd
-port
-root
-dbname
3. Connect using cursor
4. Execute an sql statement
5. Fetch your records
'''

'''
FLASK-SQLALCHEMY
    Library that helps us write classes object to communicate to our database without
    writing sql statements

    EXAMPLE 
    INSERT INTO sales VALUES (inv_id=1, quantity=10, created=now())

    create a class and it SalesModel
    then create function that inserts records
    then insert

    class SalesModel():
        def insert_sales(self):
            db.session.add()
        
    query

        def query_sales(self):
            self.query.all()

        select * from sales


    STEPS TO USE FLASK-SQLALCHEMY
    1. install it
    2. use it
        - create a connection to the db
        - load configurations
        - create an instance of FLASK-SQLALCHEMY by passing in the app
'''

#instanciating a class
app=Flask(__name__)
# load config for flask sql alchemy
app.config.from_object(Development)
'''
requirements
database://user:pwd@host:port/databasename
'''


# Instanciate sql alchemy
# comes with functions and helpers to create tables
db=SQLAlchemy(app)

# creating db connection with psychopg2
conn=psycopg2.connect("dbname='inventory_management_system' user='postgres' host='localhost' port='5432' password='root'")

cur=conn.cursor()
# creating of endpoints
# 1. declaration of the route
# 2. A function embedded
# @app.route('/')
# def helloWorld():
#     return "<h1>Welcome to web development</h1>"

# creating tables
from models.inventory import inventoryModel
from models.sales import SalesModel
from models.stock import StocksModel



@app.before_first_request
def create_table():
    db.create_all()




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
    # querying records from db
    inventories=inventoryModel.query.all()

    remaining_stock=getStock()
    # print(inventories)
#     cur.execute("""

#     SELECT inv_id,sum(quantity) as remainingstock
# FROM 
# (SELECT s.inv_id, -sum(quantity) as quantity
# 	FROM public.new_sales as s
# 	group by inv_id
	
# 	UNION ALL
# SELECT st.inv_id,sum(quantity) as quantity
	
# 	FROM public.new_stocks as st
# 	group by inv_id)
# 	as new_tables
# GROUP BY inv_id
# ORDER BY inv_id


#     """)
#     remaining_stock=cur.fetchall()
    

    # receive from a form
    if request.method=="POST":
        # print('worked')
        name=request.form['name']
        invType=request.form['invType']
        sellingPrice=request.form['sellingPrice']
        buyingPrice=request.form['buyingPrice']
        

            
                    # to add to database, assign value in form to colum name in database eg (column name)inv_type=(form field)invType
        new_inv=inventoryModel(name=name,inv_type=invType,buying_price=buyingPrice,selling_price=sellingPrice)
        new_inv.add_inventories()
       
    
        return redirect(url_for('inventory'))


    return render_template('inventory.html',inventories=inventories, remaining_stock=remaining_stock)
@app.route('/addStock/<inv_id>', methods=['GET','POST'])
def addStock(inv_id):
    print(inv_id)

    # # receive from a form
    if request.method=="POST":
        # print('worked')
        stock=request.form['stock']

        new_stock=StocksModel(inv_id=inv_id,quantity=stock)
        new_stock.add_stock()
        # print(new_stock)

        # print(stock)
    
        return redirect(url_for('inventory'))


    return render_template('inventory.html')
@app.route('/addSale/<inv_id>',methods=['POST','GET'])
def addSale(inv_id):

    # new_sale=SalesModel.query.all()
    # remaining_stock=getStock()
    # print(remaining_stock, "ghbjkml,;.")

    if request.method=="POST":
        quantity=request.form['quantity']
        
        new_sale=SalesModel(inv_id=inv_id,quantity=quantity)

        cur.execute(f""" 

           SELECT inv_id,sum(quantity) as remainingstock
FROM 
(SELECT s.inv_id, -sum(quantity) as quantity
	FROM public.new_sales as s
	group by inv_id
	
	UNION ALL
SELECT st.inv_id,sum(quantity) as quantity
	
	FROM public.new_stocks as st
	group by inv_id)
	as new_tables
	where inv_id={inv_id}

    GROUP BY inv_id;

    
        
        """)
        st=cur.fetchall()
        print(st)

        if st[0][1]>int(quantity):
            new_sale.add_quantity()
        else:
            return "Check your value"
        

        


        

    
        
        
       

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
@app.route('/view_sales,<inv_id>')
def view_sales(inv_id):
    inv=inventoryModel.query.filter_by(id=inv_id).first()
    sales=SalesModel.getSalesById(inv_id)
    totalSales=0
    for each in sales:
        quantity=each.quantity
    

    totals=inv.selling_price*quantity
    print(totals)

    


    return render_template('view_sales.html', sales=sales,inv=inv,totals=totals)

@app.route('/data_visualization')
def data_visualization():

    cur.execute("""
    
    SELECT type,COUNT(type)
	FROM public.inventories
	GROUP BY type;


    """)
    fruit_vegetable=cur.fetchall()
    print(fruit_vegetable)
    







    # initializing pie chart
    pieChart=pygal.Pie()
    # add components to piechart
    pieChart.title="Distribution of Fruits and Vegetables"
    #  Partitioning your pie chart


    # my_pie_data = [
    # {'Nairobi':50},
    # {'Mombasa': 50}

    
    
    # ]

    # for each in my_pie_data:
    #     for key, value in each.items():
    #         pieChart.add(key,value)
    
    # pieChart.add('Nairobi',140)
    # pieChart.add('Kilifi',100)
    # pieChart.add('Kwale',50)
    # pieChart.add('Mombasa',80)
    
    # my_pie_data = [
    #     ('Nairobi', 63),
    #     ('Mombasa', 20),
    #     ('Kilifi', 17),
    #     ('Machakos', 30),
    #     ('Kiambu', 7)
    # ]
    for each in fruit_vegetable:
        pieChart.add(each[0],each[1])

        pieData=pieChart.render_data_uri()


    # line graph
    cur.execute("""
    SELECT EXTRACT(MONTH FROM s.created_at)as sale_date,sum(i.selling_price*s.quantity) as total_sales
	FROM public.sales as s
	JOIN public.inventories as i on i.id=s.inv_id
	GROUP BY sale_date 
	ORDER BY sale_date ;
    
    
    """)
    monthlySales=cur.fetchall()
    print(monthlySales)
        # data = [
        #     {'month': 'January', 'total': 22},
        #     {'month': 'February', 'total': 27},
        #     {'month': 'March', 'total': 23},
        #     {'month': 'April', 'total': 20},
        #     {'month': 'May', 'total': 12},
        #     {'month': 'June', 'total': 32},
        #     {'month': 'July', 'total': 42},
        #     {'month': 'August', 'total': 72},
        #     {'month': 'September', 'total': 52},
        #     {'month': 'October', 'total': 42},
        #     {'month': 'November', 'total': 92},
        #     {'month': 'December', 'total': 102}
        # ]
    a=[]
    b=[]
    for each in monthlySales:
            x=each[0]
            y=each[1]
            a.append(x)
            b.append(y)
        

    

    line_chart = pygal.Line()
    line_chart.title = 'Total Sales'
    line_chart.x_labels = a
    line_chart.add('TotalSales', b)
    # line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
    # line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    # line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])

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


def getStock():
    cur.execute("""
     SELECT inv_id,sum(quantity) as remainingstock
FROM 
(SELECT s.inv_id, -sum(quantity) as quantity
	FROM public.new_sales as s
	group by inv_id
	
	UNION ALL
SELECT st.inv_id,sum(quantity) as quantity
	
	FROM public.new_stocks as st
	group by inv_id)
	as new_tables
GROUP BY inv_id
ORDER BY inv_id
    




    """)
    remaining_stock=cur.fetchall()

    return remaining_stock

      

    


    
    

if __name__=="__main__":
    app.run()
    




