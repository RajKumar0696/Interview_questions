# To check given number is even or odd
number = int(input("Enter your number:"))
if number % 2 == 0:
    print("given number is even number")
else:
    print("given number is odd number")

# print odd numbers and even numbers

for i in range(number):
    if i % 2 == 0:
        print("Even number:", i)


for i in range(number):
    if i % 2 != 0:
        print("Odd number is:", i)
