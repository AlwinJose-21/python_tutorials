num1 = int(input("Enter number1 "))
num2 = int(input("Enter number2 "))
num3 = int(input("Enter number3 "))
if (num1 >= num2) & (num1 >= num3):
    second_largest = max(num2, num3)
elif (num2 >= num1) & (num2 >= num3):
    second_largest = max(num1, num3)
else:
    second_largest = max(num1, num2)

print("Second largest element is ", second_largest)
