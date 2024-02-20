list1 = [12, 34, 56, 78, 2, 12, 34, 40, 2]
uniq = []
duplicate = []
for i in list1:
    if i not in uniq:
        uniq.append(i)
    else:
        duplicate.append(i)

print(uniq)
print(duplicate)
