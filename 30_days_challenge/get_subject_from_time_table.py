time = float(input("Enter time: "))
if 9 <= time <= 11:
    print("Tamil")
elif 11 <= time <= 11.15:
    print("Break")
elif 11.15 <= time <= 1:
    print("English")
elif 1 <= time <= 2:
    print("Lunch")
elif 2 <= time <= 4:
    print("maths")
else:
    print("School finished")
