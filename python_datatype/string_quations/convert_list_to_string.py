list1 = ["apple", "ball", "cat", "elefant"]
list2 = ["A", "B", "C", "D", "E"]

string = ''
for i in list1:
    string = string + i
print(type(string))

print(",".join(list1))
print('\n'.join(list1))

new_dict = {}
for i in range(len(list1)):
    new_dict.update({list2[i]: list1[i]})
print(new_dict)
