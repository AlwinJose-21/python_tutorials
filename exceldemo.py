f=open('C:/Users/Hp/Downloads/movies_cleaned_pandas.csv')
for i in f:
    data=i.rstrip('\n').split(',')
    year=data[2]
    if year>'2005':
        print(data[1:4])
