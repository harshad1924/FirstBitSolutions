#Write a program to check if user has entered correct userid and password.
userid = "admin"
password = "1234"


username = input("Enter UserId: ")
passw = input("Enter Password: ")

if(username == userid and password == passw):
    print("Valid username and password")

else:
    print("Invalid Userid or Password")