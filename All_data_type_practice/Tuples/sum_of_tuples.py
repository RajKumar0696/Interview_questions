x = (1, 2, 3, 4)
y = (3, 5, 2, 1)
z = (2, 2, 3, 1)
sum_of = []
for i in range(len(x)):
    sum_of.append(x[i] + y[i] + z[i])
print(tuple(sum_of))
print(sum_of)

# Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples.
nums = [(1, 2), (2, 3), (3, 4)]
list1 = []
for i in nums:
    list1.append(sum(i))
print(list1)