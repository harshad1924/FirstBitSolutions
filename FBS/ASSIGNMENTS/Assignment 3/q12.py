# Write a program to check if given 3 digit number is a palindrome or not.
num = int(input("Enter A number: "))

original = num

digit1 = (num % 10) * 100
digit2 = ((num//10) % 10) * 10
digit3 = num // 100

reverse = digit1 + digit2 + digit3

if(reverse == original):
    print("Palindrome")
else:
    print("Not Palindrome")