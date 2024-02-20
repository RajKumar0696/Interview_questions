number = int(input("Enter number: "))
temp = number
value = 0
while number != 0:
    digit = number % 10
    value = value + digit ** 3
    number = number // 10
if value == temp:
    print("armstrong", value)
else:
    print("no", value)
