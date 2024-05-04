#4 subject
sub1=int(input("Enter your mark in subject1:"))
sub2=int(input("Enter your marks in subject 2"))
sub3=int(input("Enter your mark in subject3"))
sub4=int(input("Enter your mark in subject4"))
total=sub1+sub2+sub3+sub4
if(total>180):
    print("A+")
elif(total<=179)&(total>=160):
    print("A")
elif(total<=159)&(total>=140):
    print("B+")
elif(total<=139)&(total>=120):
    print("B")
elif(total<=119)&(total>=100):
    print("C+")
elif(total<=99)&(total>=88):
    print("C")
else:
    print("Fail")