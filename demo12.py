f = open('C:/Users/Hp/Downloads/customer1.txt', 'r')
for i in f:
    data = i.rstrip('\n').split(',')
    prof = data[-2]
    if prof == 'Dancer':
        print(data[1:4])
