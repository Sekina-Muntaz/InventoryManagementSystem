my_pie_data = [
        ('Nairobi', 63),
        ('Mombasa', 20),
        ('Kilifi', 17),
        ('Machakos', 30),
        ('Kiambu', 7)
    ]
print(my_pie_data[0])
for each in my_pie_data:
    print(each[0],each[1])


data = [
        {'month': 'January', 'total': 22},
        {'month': 'February', 'total': 27},
        {'month': 'March', 'total': 23},
        {'month': 'April', 'total': 20},
        {'month': 'May', 'total': 12},
        {'month': 'June', 'total': 32},
        {'month': 'July', 'total': 42},
        {'month': 'August', 'total': 72},
        {'month': 'September', 'total': 52},
        {'month': 'October', 'total': 42},
        {'month': 'November', 'total': 92},
        {'month': 'December', 'total': 102}
    ]
a=[]
b=[]
for each in data:
    x=each["month"]
    y=each["total"]
    a.append(x)
    b.append(y)

print(a)
print(b)

    
#     # for key,value in each.items():
#     #     print()
        
