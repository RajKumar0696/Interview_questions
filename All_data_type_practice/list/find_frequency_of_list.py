list1 = [1, 2, 3, 4, 5, 6, 1, 3, 5, 7, 8, 4, 0]
uniq = []
for i in list1:
    if i not in uniq:
        uniq.append(i)
for i in uniq:
    count = 0
    for j in list1:
        if i == j:
            count = count + 1
    print(i, count)
