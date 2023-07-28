# Change the element 35 to 3500

list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]
list1[1][2][2][1] = 3500
print(list1)
for i in list1:
    if i == 35:
        print(i)
        i = 3500
        list1.append(i)
        break
print(list1)
