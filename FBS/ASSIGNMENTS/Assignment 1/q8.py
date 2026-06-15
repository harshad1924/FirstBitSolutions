days = int(input("Enter number of days: "))

years = days // 365
remaining_days = days % 365

weeks = days // 7
remaining_days_after_weeks = days % 7
print("Years:", years)
print("Remaining days after calculating years:", remaining_days)
print("Weeks:", weeks)
print("Remaining days after calculating weeks:", remaining_days_after_weeks)