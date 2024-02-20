L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d',)]
l1 = []
for i in L:
    if len(i) == 0:
        continue
    else:
        l1.append(i)
print(l1)

# method 2
L = [t for t in L if t]
print(L)
