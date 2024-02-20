num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))

if num1 < num2:
    large = num2
else:
    large = num1
for i in range(1,large+1):
    if large % num1 == 0 and large % num2 == 0:
        lcm = i
print(i)