num = int(input("Enter your number:"))
factorial = 1
if num > 1:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The", num, "factorial is:", factorial)
