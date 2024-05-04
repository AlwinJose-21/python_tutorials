f=open('C:/Users/Hp/Downloads/customer1.txt','r')
dic={}
for i in f:
    data=i.rstrip('\n').split(',')
    country=data[-1]
    if country not in dic:
        dic[country]=1
    else:
        dic[country]+=1
for k,v in dic.items():
    print(k,":",v)