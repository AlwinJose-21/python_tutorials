f = open('C:/Users/Hp/Downloads/movies_cleaned_pandas.csv')
for i in f:
    data = i.rstrip('\n').split(',')
    rating = data[3]
    year = data[2]
    if rating > '3' and year > '2007':
        print(data[1:4])
