year = int(input("Enter year:"))
if year % 400 == 0 and year % 4 == 0 and year % 100 != 0:
    print("year is leap", year)
else:
    print("not leap year", year)