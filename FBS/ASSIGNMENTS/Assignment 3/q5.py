#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle

angle1 = int(input("Enter angle1: "))
angle2 = int(input("Enter angle2: "))
angle3 = int(input("Enter angle3: "))

if angle1 + angle2 + angle3 != 180:
    print("Invalid Triangle")

elif angle1 == angle2 and angle2 == angle3:
    print("Equilateral Triangle")

elif angle1 == angle2 or angle2 == angle3 or angle1 == angle3:
    print("Isosceles Triangle")

else:
    print("Scalene Triangle")