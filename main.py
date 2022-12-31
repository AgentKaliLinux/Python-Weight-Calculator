#It Is The Weight Calculator.............

print("Enter Your Name")
b = input() #First Of All You Need To Enter Your Name........
print("Enter Your Weight")
x = int(input()) #Then You Need To Enter Your Weight.........

if x>=25 and x<=40:
    print(b + " is very thin Person")
elif x>=45 and x<=60:
    print(b + " is a Normal Person")
elif x>=60 and x<=80:
    print(b + " is a UpperWeight Person")
elif x>=80 and x<=120:
    print(b + " is a OverWeight Person")
else:
    print(b + " is a Obesity Person")

#Thats The End Of Calculator..........Hope You Like It.........