f=open('C:/Users/Hp/Downloads/customer1.txt','r')
for i in f:
    data=i.rstrip('\n').split(',')
    age=data[3]
    country=data[-1]
    if age>'50' and country=='india':
        print(data[1::2])