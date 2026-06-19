# Write a program to calculate profit or loss.
cp = int(input("Enter cost price: "))
sp = int(input("Enter seling price: "))

if(sp > cp):
    profit = sp - cp
    print(f"Profit of {profit}")
elif(cp == sp):
    print("No loss or profit")
else:
    loss = cp - sp
    print(f"Loss of {loss}")  