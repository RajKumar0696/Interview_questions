number = 5
for row in range(number):
    for column in range(number - row):
        print(" ", end=" ")
    for column in range(2 * row + 1):
        if column == 0 or column == 2 * row or row == number - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("\r")
