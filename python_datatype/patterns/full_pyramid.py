number = int(input("Enter row number:"))
for row in range(number):
    gap = number - row
    for column in range(gap):
        print(" ", end=" ")
    star = 2 * row + 1
    for column in range(star):
        print("*", end=" ")
    print("\r")
