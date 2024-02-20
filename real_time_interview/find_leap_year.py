number = int(input("Enter your year:"))
if number % 400 == 0 and number % 100 == 0:
    print(number, "is leap year")
elif number % 4 == 0 and number % 100 != 0:
    print(number, "is leap year")
else:
    print(number, "is not leap year")

