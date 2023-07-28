number = int(input("Enter number of rows:"))
for rows in range(number, 0, -1):
    for columns in range(rows):
        print("* ", end="")
    print("\r")

rows = int(input("Enter your rows number:"))
x = 0
for i in range(rows + 1, 0, -1):
    x = x + 1
    for j in range(0, i - 1):
        print(x, end=" ")
    print("\r")
