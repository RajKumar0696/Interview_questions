number = int(input("Enter number 0f rows:"))
gap = number - 1
for row in range(number,0,-1):
    for column in range(gap):
        print(end=" ")
    gap = gap + 1
    for column in range(row):
        print("*", end="")
    print("\r")

