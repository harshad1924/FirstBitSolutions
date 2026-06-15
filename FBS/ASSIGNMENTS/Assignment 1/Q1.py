maths = int(input("Enter marks in Maths: "))
science = int(input("Enter marks in Science: "))
english = int(input("Enter marks in English: "))    
marathi = int(input("Enter marks in Marathi: "))
sst = int(input("Enter marks in SST: "))

total_marks = maths + science + english + marathi + sst
percentage = (total_marks / 500) * 100
print("percentage is", percentage)