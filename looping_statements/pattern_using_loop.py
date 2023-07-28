number = 5
for row in range(number):
    gap = number - row
    for column in range(0, gap):
        print(end=" ")
    star = 2 * row + 1
    for column in range(star):
        print("*", end="")
    print("\r")

for row in range(number):
    for column in range(row + 1):
        if row == 0 or row == number - 1 or column == 0 or column == row:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("\r")

for row in range(number):
    for column in range(row+1):
        print("*", end=" ")
    print("\r")
gap = number - 1
for row in range(number):
    for column in range(gap+1):
        print(end=" ")
    gap = gap - 1
    for column in range(row+1):
        print("*", end="")
    print("\r")

number = 123456
reverse = 0

while number != 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10
print(reverse)