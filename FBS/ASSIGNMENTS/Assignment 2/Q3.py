feet = int(input("Enter distance in feet: "))
inches = int(input("Enter distance in inches"))

total_inches = (feet * 12) + inches
cm = total_inches * 2.54
m = cm / 100

print(f"centimeters and meters are {cm} and {m} resp.")