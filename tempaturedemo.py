f=open('C:/Users/Hp/Downloads/temper')
dic={}
for i in f:
    data=i.rstrip('\n').split(',')
    dist=data[0]
    temp=data[1]
    if dist not in dic:
        dic[dist]=temp
    else:
        old=dic[dist]
        if temp>old:
            dic[dist]=temp
        else:
            dic[dist]=old
for k,v in dic.items():
    print(k,":",v)

