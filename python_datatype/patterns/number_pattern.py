# 5
# 54
# 543
# 5432
# 54321
number = 5
for i in range(number):
    x = 5
    for j in range(i+1):
        if i == 0 or j == 0 or i == number - 1 or j == i:
            print(x, end=" ")
            x = x - 1
        else:
            print(" ", end=" ")
    print("\r")
