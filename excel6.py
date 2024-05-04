f=open('C:/Users/Hp/Downloads/movies_cleaned_pandas.csv')
dic={}
for i in f:
    data=i.rstrip('\n').split(',')
    year=data[2]
    if year not in dic:
        dic[year]=1
    else:
        dic[year]+=1
for k,v in dic.items():
    print(k,":",v)
