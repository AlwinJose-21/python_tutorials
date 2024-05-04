f = open('C:/Users/Hp/Downloads/customer1.txt', 'r')
for i in f:
    data = i.rstrip('\n').split(',')
    country = data[-1]
    prof = data[-2]
    if country == 'india' and prof == 'Dancer':
        print(data)
