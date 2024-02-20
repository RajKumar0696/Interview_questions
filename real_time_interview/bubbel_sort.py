list1 = [21, 4, 65, 8, 9, 90, 43, 56, 10]
for i in range(len(list1)-1,0,-1):
    for j in range(i):
        if list1[j]> list1[j+1]:
            temp = list1[j]
            list1[j] = list1[j+1]
            list1[j+1]= temp
print(list1)
list1.sort(reverse=False)
print(list1)
