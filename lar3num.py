num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))
num3=int(input("Enter number3:"))
if(num1>num2>num3):
    print("largest number is",num1)
elif(num1<num2>num3):
    print("largest number is",num2)
else:
    print("largest number is",num3)
