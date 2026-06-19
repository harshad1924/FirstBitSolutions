#Input 5 subject marks from user and display grade(eg.First class,Second class ..)

maths = int(input("Enter maths marks: "))
science= int(input("Enter science marks: "))
marathi = int(input("Enter marathi marks: "))
sst = int(input("Enter sst marks: "))
english = int(input("Enter english marks: "))

total_marks = maths + science + marathi + sst + english
total_percentage = (total_marks / 500) * 100

if(total_percentage > 80):
    print(f"Firstclass with {total_percentage}%")
elif(total_percentage > 60):
    print(f"Second Class with {total_percentage}%")
elif(total_percentage > 40):
    print(f"Third Class")
else:
    print("FAIL")