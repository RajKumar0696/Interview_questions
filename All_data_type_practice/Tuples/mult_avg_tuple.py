str1 = "python 3.0"
print(tuple(str1.replace(" ", "")))


def average(new_tup):
    avg = []
    for i in new_tup:
        avg.append(sum(i) / len(i))
    return avg


new_tup = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
print(average(new_tup))
print(average(((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
              ))

# multiple
new_tuple = (2, 4, 8, 8, 3, 2, 9)
mult = 1
for i in new_tuple:
    mult = mult * i
print(mult)

# Write a Python program to convert a tuple of string values to a tuple of integer values.
tuple_str = (('333', '33'), ('1416', '55'))
result = tuple((int(x[0]), int(x[1])) for x in tuple_str)
print(result)

# Write a Python program to convert a given tuple of positive integers into an integer.
nums = (10, 20, 30)
tot = ""
for i in nums:
    tot = tot + str(i)
print(tot)
