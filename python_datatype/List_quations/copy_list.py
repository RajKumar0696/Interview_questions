list1 = [12, 45, 46, 12, 48, 98, 76, 54, 10]
list2 = list1.copy()
print(list2)


list1 = [12, 45, 46, 12, 48, 98, 76, 54, 10, list2]
print(list2)

list1 = [12, 45, 46, 12, 48, 98, 76, 54, 10]
list2 = list1[:]
print(list2)