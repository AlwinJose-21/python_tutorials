salary=int(input("Enter your salary:"))
service=int(input("Years of experience:"))
if(service>5):
    bonus=salary*5/100
    print("Your net bonus is",bonus)
else:
    print("No bonus")