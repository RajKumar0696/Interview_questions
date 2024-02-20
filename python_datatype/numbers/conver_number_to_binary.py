number = temp = int(input("Enter num1:"))

binary = ""
while temp>0:
    remainder = temp % 2
    binary = str(remainder) + binary
    temp = temp // 2
print(binary)

decimal = int(input("Please Enter a decimal number: "))
binary = bin(decimal)
print("Binary number is ", binary[2:], " for ", decimal)