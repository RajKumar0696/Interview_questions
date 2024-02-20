new_dict = {'ravi': 10, 'raj': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
list1 = list(new_dict.keys())
list1.sort()
reversed_dict = {}
for i in list1:
    reversed_dict.update({i: new_dict[i]})
print(reversed_dict)

sorte = sorted(new_dict.items())
print(dict(sorte))
