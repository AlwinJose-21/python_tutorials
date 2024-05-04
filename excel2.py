f = open('C:/Users/Hp/Downloads/movies_cleaned_pandas.csv')
for i in f:
    data = i.rstrip('\n').split(',')
    rating = data[3]
    if rating > '4':
        print(data[1:])
