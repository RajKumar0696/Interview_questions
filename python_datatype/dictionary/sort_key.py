key_value = {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323, 10: 33}
print(key_value)
list1 = list(key_value.keys())
list2 = list(key_value.values())
list1.sort()
list2.sort()
new = {}
for i in list1:
    for j in list2:
        new.update({key_value[i]: i})
print(new)
