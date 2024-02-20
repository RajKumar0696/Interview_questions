base_num = int(input("Enter base number:"))
exponent_num = int(input("Enter exponent number:"))
power = 1
for i in range(exponent_num):
    power = power * base_num
print(power)
    