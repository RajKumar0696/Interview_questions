list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = ['d', 'e', 'f', 'g', 'h']

missing_value = []
additional_value = []
for i in list1:
    if i not in list2:
        missing_value.append(i)
for i in list2:
    if i not in list1:
        additional_value.append(i)

print(missing_value)
print(additional_value)
