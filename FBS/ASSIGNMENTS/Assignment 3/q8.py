#8. Write a program to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter thesame. If user enters the same number then show him success message otherwise failed. (Something like captcha)

userid = "admin"
password = "1234"
captcha = "czpab"

username = input("Enter UserId: ")
passw = input("Enter Password: ")

if(username == userid and password == passw):
    print("Valid username and password")
    print(captcha)
    c = (input("Enter the captcha: "))
    if(captcha == c):
        print("Correct captcha")
else:
    print("Invalid Userid or Password")