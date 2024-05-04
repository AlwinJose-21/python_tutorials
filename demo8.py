f = open('C:/Users/Hp/Downloads/customer1.txt', 'r')
for i in f:
    data = i.rstrip('\n').split(',')
    age = data[3]
    if age > '60':
        print(data[1:5])
