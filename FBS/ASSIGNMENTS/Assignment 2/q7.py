num = int(input("Enter a three digit number: ")) #123

rem = num % 10 # 3
quo = num // 10 # 12
digit = quo % 10 # 2
num = quo // 10 # 1
remain = num % 10  # 1

total = rem + digit + remain 

print("total sum is " , total) # 6