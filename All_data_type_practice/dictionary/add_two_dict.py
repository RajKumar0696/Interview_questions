d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400, 'e': 100, 'f': 200, 'c': 300}
new_dict = {}
for i in d1:
    if i in d2:
        new_dict.update({i: d1[i] + d2[i]})
    # else:
    #     new_dict.update({i: d1[i]})
for j in d2:
    if j not in new_dict:
        new_dict.update({j: d2[j]})
print(new_dict)

# in build methods
from collections import Counter

result = Counter(d1) + Counter(d2)
print(result)
