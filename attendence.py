num=int(input("Number of classes held:"))
att=int(input("Number of classes attened:"))
per=att/num*100
print("Percentage of class attended:",per,"%")
if(per>=75):
    print("Student is allowed to sit in exam")
else:
    print("Student should not sit in exam.")
