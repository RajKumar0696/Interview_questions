number = int(input("Enter number of rows:"))
for rows in range(number):
    for column in range(number):
        print("*", end=" ")
    print("\r")

