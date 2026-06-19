cp = int(input("Enter Cost price of book: "))
discount = int(input("Enter Discount% to be given: "))

disc_amt = cp * discount / 100
sp = cp - disc_amt

print(f"Selling price after discount is {sp}")