list1 = [12, 45, 46, 12, 48, 98, 76, 54, 10]
list1.sort()
print(list1)
print("The smallest number is:", list1[0])
print("The biggest number is:", list1[-1])
minimum = list1[0]
for i in range(len(list1)):
    if list1[i] < minimum:
        minimum = list1[i]
print("The min num is:", minimum)


maximum = list1[0]
for i in range(len(list1)):
    if list1[i] > maximum:
        maximum = list1[i]
print("The max num is:",maximum)