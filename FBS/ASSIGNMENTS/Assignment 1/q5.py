principle = int(input("Enter principle amount: "))
rate = int(input("Enter rate of interest: "))
time = int(input("Enter time in years: "))
compound_interest = principle * (1 + rate / 100) ** time - principle
print("Compound interest is", compound_interest)