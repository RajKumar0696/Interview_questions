rows = int(input("Enter your rows number:"))
for i in range(rows):
    for j in range(i + 1):
        if i == 0 or i == rows - 1 or j == 0 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("\r")

