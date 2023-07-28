number = int(input("Enter row number:"))
for row in range(number):
    gap = number - row
    for column in range(gap):
        print(end=" ")
    star = 2 * row + 1
    for column in range(0, star):
        print("*", end="")
    print("\r")

for row in range(number):
    gap = number - row
    for column in range(gap):
        print(end=" ")
    star = 2 * row + 1
    for column in range(0, star):
        print("*", end="")
    print("\r")
k = number - 1
for i in range(number):

    for j in range(k):
        print(end=" ")
    k = k - 1
    for j in range(i+1):
        print("*", end="")
    print("\r")

rows = int(input("Please Enter Rows  : "))
columns = int(input("Please Enter Columns  : "))

print("Rectangle Star Pattern")
for i in range(rows):
    for j in range(columns):
        print('*', end=' ')
    print()
