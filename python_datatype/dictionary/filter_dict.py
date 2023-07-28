d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}
l1 = ['A', 'C', 'F']
d2 = {}
for i in l1:
    d2.update({i: d1[i]})
print(d2)

new_dict = {key: d1[key] for key in l1}
