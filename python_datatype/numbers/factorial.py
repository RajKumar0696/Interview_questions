number = int(input("Enter number:"))
factorial = 1
if number > 0:
    for i in range(1, number + 1):
        factorial = factorial * i
    print("given {} factorial is:{}".format(number, factorial))
