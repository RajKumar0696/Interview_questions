num1 = 10
num2 = 23

while num2 != 0:
    temp = num1 & num2
    num1 = num1 ^ num2
    num2 = temp << 1
print(num1)

