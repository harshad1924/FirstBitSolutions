#3. Write a program to input angles of a triangle and check whether triangle is valid or not.

angle1 = int(input("Enter angle1: "))
angle2 = int(input("Enter angle2: "))
angle3 = int(input("Enter angle3: "))

traingle = angle1 + angle2 + angle3

if(traingle == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0):
    print("Valid Triangle")

else:
    print("Invalid Triangle")