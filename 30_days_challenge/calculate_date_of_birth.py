from datetime import date

today_date = date.today()
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

DOB = date(year, month, day)
day_diff = today_date - DOB
print("Number of days: ", day_diff)
print("Number of month: ", (day_diff // 365)*12)
print("Number of years: ", (day_diff // 365))
print("Number of seconds: ", (day_diff*60*60))
