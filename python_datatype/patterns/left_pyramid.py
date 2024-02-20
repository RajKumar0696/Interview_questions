number = int(input("Enter row number:"))
gap = number - 1
for row in range(number):
    for column in range(0, gap):
        print(end=" ")
    gap = gap - 1
    for column in range(row+1):
        print("*", end="")

    print("\r")
number= 5
gap = number - 1
for row in range(number):
    for column in range(0, gap):
        print(end=" ")
    gap = gap - 1
    for column in range(row + 1):
        print("*", end="")
    print("\r")