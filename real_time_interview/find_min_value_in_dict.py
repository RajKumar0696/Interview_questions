dict1 = {'English': 62, 'Math': 55, 'Chemistry': 85}
minimum = min(dict1.values())
print(minimum)

sample_dict = {'a': 403, 'b': 40, 'd': 4300, 'c': 2300}
list1 = list(sample_dict.values())
minimum = list1[0]
min_inx = 0
for i in range(len(list1)):
    if list1[i] < minimum:
        minimum = list1[i]
        min_inx = i
print(list(sample_dict)[min_inx], minimum)
