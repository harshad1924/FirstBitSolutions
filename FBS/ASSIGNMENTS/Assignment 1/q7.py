a = int(input("Enter a coefficientn a: "))
b = int(input("Enter a coefficientn b: "))
c = int(input("Enter a coefficientn c: "))
discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    print("Roots are real and different.")
    print("Root 1:", root1)
    print("Root 2:", root2)