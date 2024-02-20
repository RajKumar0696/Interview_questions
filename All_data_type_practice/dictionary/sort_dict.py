num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
sorted_dict = {x: sorted(y) for x, y in num.items()}
print(sorted_dict)
for i in num.values():
    n1 = i
    for k in range(len(n1) - 1, 0, -1):
        for j in range(k):
            if n1[j] > n1[j + 1]:
                temp = n1[j]
                n1[j] = n1[j + 1]
                n1[j + 1] = temp
print(num)
