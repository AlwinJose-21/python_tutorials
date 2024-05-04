cost = int(input("Enter cost price of the bike Rs:"))
if cost > 100000:
    tax = cost * 0.15
elif cost >= 50000:
    tax = cost * 0.10
else:
    tax = cost * 0.05
print("Road tax is Rs", tax)
