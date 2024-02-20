d = {'1': ['a', 'b'], '2': ['c', 'd']}
# ac
# ad
# bc
# bd
list1 = list(d["1"])
list2 = list(d["2"])

for i in list1:
    for j in list2:
        print(i+j)


