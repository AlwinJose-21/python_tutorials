f=open('C:/Users/Hp/Downloads/movies_cleaned_pandas.csv')
for i in f:
    data=i.rstrip('\n').split(',')
    year=data[2]
    if year>'1975' and year<'2000':
        print(data[1:4])
