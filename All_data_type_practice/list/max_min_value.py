list1 = [100, 30, 40, 37, 59, 64]
minimum = list1[0]
for i in range(len(list1)):
    if list1[i] < minimum:
        minimum = list1[i]
print(minimum)

maximum = list1[0]
for i in range(len(list1)):
    if list1[i] > maximum:
        maximum = list1[i]
print(maximum)
