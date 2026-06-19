#Write a program to input all sides of a triangle and check whether triangle is valid or not.

a = int(input("Enter side of triangle: "))
b = int(input("Enter side of triangle: "))
c = int(input("Enter side of triangle: "))

if(a + b > c and b + c > a and c + a > b):
    print("Valid triangle")
else:
    print("Invalid triangle")