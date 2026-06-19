#Write a program to input any alphabet and check whether it is vowel or consonant.

alphabet = input("Enter a charecter: ")

if (alphabet in "aeiouAEIOU"):
    print("It is a vowel")
else:
    print("It is a consonent")