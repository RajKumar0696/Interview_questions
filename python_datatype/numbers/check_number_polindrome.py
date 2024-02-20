number = int(input("Enter your number:"))
tem = number
print(number)
rev = 0
while number != 0:
    digit = number % 10
    rev = rev * 10 + digit
    number = number // 10
if tem == rev:
    print("number is palindrome")
else:
    print("no")
