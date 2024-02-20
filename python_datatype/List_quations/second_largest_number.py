list1 = [12, 45, 46, 12, 48, 98, 98, 54, 10]
list1.sort()
print(list1[-2])


second_max = list1[0]
for i in range(len(list1)):
    if list1[i] > second_max:
        second_max = list1[i-1]
print(second_max)
