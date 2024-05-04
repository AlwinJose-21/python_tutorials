lst=[]
f=open('numbers','r')
for i in f:
    lst.append(int(i.rstrip('\n')))
print(sum(lst))
# data='hello\n'
# data1=data.rstrip('o\n')
# print(data1)
