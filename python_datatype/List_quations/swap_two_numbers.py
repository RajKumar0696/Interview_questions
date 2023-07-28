# swapping two number using third variable
num1 = int(input("Enter number 1:"))
num2 = int(input(" Enter number 2:"))
num = num1
num1 = num2
num2 = num
print("num1 is:", num1)
print("num2 is:", num2)

# swapping two numbers without using third variable
num1 = int(input("Enter number 1:"))
num2 = int(input(" Enter number 2:"))
num1, num2 = num2, num1
print("num1 is:", num1)
print("num2 is:", num2)
