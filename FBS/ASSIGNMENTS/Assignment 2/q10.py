num = int(input("Enter a number: "))

digit1 = (num % 10) * 100
digit2 = ( (num // 10) % 10 ) * 10
digit3 = num // 100 

reverse = digit1 + digit2 + digit3

print("Reverse number is : ", reverse)