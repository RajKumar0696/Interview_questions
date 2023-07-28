# MAP() Function-
# The Map() function takes a function and a list as input.
# Map() performs an operation on the entire list and return the result in a new list
# Syntax-map(function/lambda, list)

# Filter() Function-
# Filter() is used to create a list of elements for which a function returns “True”.
# Syntax-filter( function that returns True, list)

# Lambda() Function
# Lambda function mainly used to create a function without a name
# It is mainly used with filter() and map() functions.
# It can receive any number of arguments, but can only have one expression.

#
# # simple lambda function
# add = lambda x: x * 2
# print(add(10))
#
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#
# # PRINT EVEN NUMBER USING LAMBDA
# even_number = list(filter(lambda x: x % 2 == 0, number))
# print(even_number)
#
# # print odd number using lambda
# odd_number = list(filter(lambda i: i % 2 != 0, number))
# print(odd_number)
#
# # map using lambda
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# even_number = list(map(lambda x: x % 2 == 0, number))
# print(even_number)
#
# # multiple two numbers using lambda
# num1 = [10, 20, 30]
# num2 = [20, 30, 40]
# multi = list(map(lambda x, y: x * y, num1, num2))
# print(multi)
#
# num1 = int(input("Enter num1:"))
# num2 = int(input("Enter num2:"))
# multy = lambda x, y: x * y
# print(multy(num1, num2))

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10, 23]
list3 = []
for i in range(len(list1)):
    add = list1[i] + list2[i]
    list3.append(add)
print(list3)

added = list(map(lambda x, y: x + y, list2, list1))
print(added)


# Write a function that takes an argument and returns its cubic value.
# Define a list of integers ranging from -10 to 10.
# Apply the function to the entire list and generate a new output list.
def cubic(x):
    return x * x * x


# number = list(range(-10, 11))
# print(number)
list1 = []
for i in range(-10, 11):
    list1.append(i)
print(list1)

new_output_list = list(map(cubic, list1))
print(new_output_list)

# return price grater than or equal 56
price = [12, 3, 45, 6, 78, 90, 45, 32, 19, 56, 100]
grater_price = list(filter(lambda x: x >= 30, price))
grater_price.sort()
print(grater_price)

# Write a code that takes the range from the user (ie upper and lower bound) and
# returns a list of positive and even numbers only-
lower = int(input("Enter minimum number:"))
upper = int(input("Enter maximum number:"))
range_of = range(lower, upper)

list1 = list(filter(lambda x: x >= 0 and x % 2 == 0, range_of))
print(list1)
