f=open('C:/Users/Hp/Downloads/customer1.txt','r')
for i in f:
    data=i.rstrip('\n').split(',')
    age=data[3]
    if age>'50':
        print(data)