# Exercise 2: Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = list(map(lambda x, y: x + y, list1, list2))
print(list3)

list3 = []
length = len(list1)
for i in range(length):
    add = list1[i] + list2[i]
    list3.append(add)
print(list3)

# Exercise 4: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = []
for i in list1:
    for j in list2:
        list3.append(i + j)
print(list3)


list3 = [i + j for i in list1 for j in list2]
print(list3)
