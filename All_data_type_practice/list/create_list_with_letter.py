number = 5
list1 = ['p', 'q']
list2 = []
for i in range(1, number+1):
    for j in list1:
        word = str(i) + j
        list2.append(word)
print(list2)

