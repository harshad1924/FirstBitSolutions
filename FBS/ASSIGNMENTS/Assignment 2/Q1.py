hours = int(input("Enter hh:"))
minutes = int(input("Enter min:"))
seconds = int(input("Enter Sec:"))

hours_seconds = 3600 * hours
mins_seconds = 60 * minutes
seconds_seconds = seconds

totalseconds = hours_seconds + mins_seconds + seconds

print(f"hh,mins,seconds = {hours_seconds},{mins_seconds},{seconds_seconds}")
print("Total seconds: ",totalseconds)