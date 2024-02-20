list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [1, 3, 5, 8, 0, 10]
common = []
for i in list1:
    if i in list2:
        common.append(i)
print(common)
