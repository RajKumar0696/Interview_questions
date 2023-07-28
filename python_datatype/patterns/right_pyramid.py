number = int(input("Enter your rows number:"))
num = 65
for rows in range(number):
    for column in range(rows+1):
        ch = chr(num)
        print(ch, end="")
        num = num + 1
    print("\r")

gap = number - 1
for i in range(number):
    for j in range(gap):
        print(end=" ")
    gap = gap - 1
    for j in range(i + 1):
        print("*", end="")
    print("\r")

#
# x = 1
# for rows in range(number, 0, -1):
#     # x = 1
#     for column in range(rows):
#         print(x, end=" ")
#         x = x - 1
#     print("\r")
