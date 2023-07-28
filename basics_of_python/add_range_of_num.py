# Write a program to iterate the first 10 numbers and in each iteration,
# print the sum of the current and previous number.
num = 10
previous_num = 0
for number in range(0, num+1):
    sum_of = previous_num + number
    print("current number", number, "previous number", previous_num, "sum of", sum_of)
    previous_num = number


# Given two integer numbers return their product only if the product is equal to or lower than 1000,
# else return their sum.
# def mult_add(num1, num2):
#     product = num1 * num2
#     if product <= 1000:
#         print("The product mult is:", product)
#     else:
#         sum_of = num1 + num2
#         print("The sum is:", sum_of)
#
#
# mult_add(40, 30)

# Write a program to accept a string from the user and
# display characters that are present at an even index number.

user_given_string = input("Enter your string:")
even_string = user_given_string[0::2]

for i in user_given_string[0::2]:
    print(i)


# Write a program to remove characters from a string starting from zero up to n and return a new string.
user_string = input("Enter string:")
number = int(input("Enter your number:"))

new_string = user_string[number:]
print(new_string)
