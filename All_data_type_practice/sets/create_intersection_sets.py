# Write a Python program to create an intersection of sets.
# intersection gives common values from two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 60, 70, 40, 10}
set3 = set1 & set2
print(set3)

# Write a Python program to create a union of sets.
# union gives without duplicate value from two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 60, 70, 40, 10}
set3 = set1.union(set2)
print(set3)

# Write a Python program to create set difference.
#  difference will give diff of two sets based on condition
set1 = {10, 20, 30, 40, 50}
set2 = {30, 60, 70, 40, 10}
set3 = set2.difference(set1)
print(set3)

# Write a Python program to create a symmetric difference
# symmetric diff will give uniq values in two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 60, 70, 40, 10}
set4 = set1.symmetric_difference(set2)
print(set4)

# Write a Python program to create a shallow copy of sets.
# shallow copy will give exact value of given set
set1 = {"Red", "Green"}
set2 = {"Green", "Red"}
set3 = set2.copy()
print(set3)

# Write a Python program to check if two given sets have no elements in common.
x = {1, 2, 3, 4}
print(x)
y = {4, 5, 6, 7}
z = {8}

# isdisjoint will return boolean in based on condition (if any one value is matched return false)
print(x.isdisjoint(y) and x.isdisjoint(z))
print(y.isdisjoint(x) and y.isdisjoint(z))
print(z.isdisjoint(x) and z.isdisjoint(y))

# Write a Python program to remove the intersection of a second set with a first set.
# difference_update will give same as difference but one thing find the diff both sets in single condition
sn1 = {1, 2, 3, 4, 5}
sn2 = {4, 5, 6, 7, 8}
sn1.difference_update(sn2)
print(sn1)
print(sn2)
# method2
sn1 -= sn2
print(sn1)
print(sn2)
