# unpack tuple
new_tuple = 12, 10, 20
n1, n2, n3 = new_tuple
print(n1 + n2 + n3)

# Write a Python program to add an item to a tuple
tuple1 = (10, 11, 12, 13, 14)
print("original", tuple1)
tuple1 = tuple1 + (10,)
print("after add", tuple1)
tuple1 = tuple1[:5] + (15, 16, 17)
print("after add more than numbers", tuple1)

# Write a Python program to convert a tuple to a string.
tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str1 = "".join(tup)
print(str1)


# Write a Python program to get the 4th element from the last element of a tuple.
tuple1 = (10, 11, 12, 13, 14)
print("4th element is:", tuple1[3])
print("4th negative element:", tuple1[-4])
