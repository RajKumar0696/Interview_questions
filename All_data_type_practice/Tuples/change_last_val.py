l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([t[:-1] + (100,) for t in l])

for i in l:
    list1 = list(i)
    list1[-1] = 100
    print(tuple(list1), end="")

