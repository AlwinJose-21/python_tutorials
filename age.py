current_year=int(input("Enter current year:"))
current_month=int(input("Enter current month(1-12):"))
current_date=int(input("Enter current date(1-31):"))
birth_year=int(input("Enter birth year:"))
birth_month=int(input("Enter birth month(1-12):"))
birth_date=int(input("Enter birth date(1-31):"))
if(birth_year<=current_year)&(birth_month<=current_month)&(birth_date<=current_date):
    age=current_year-birth_year
else:
    age=current_year-birth_year-1
print("Age ",age)