Unit = int(input("Enter the unit of electricity used"))
if Unit <= 100:
    print("Free of charge")
elif (Unit > 100) & (Unit <= 200):
    charge = 5 * (Unit - 100)
    print("Charge is", charge)
else:
    charge = 10 * (Unit - 200) + 500
    print("Charge is", charge)
