list1 = [12, 3, 56, 2, 4, 67, 78, 21, 23]

# # selection sort ascending order
# for i in range(len(list1)):
#     minimum = i
#     for j in range(i+1, len(list1)):
#         if list1[minimum] > list1[j]:
#             minimum = j
#     list1[i], list1[minimum] = list1[minimum], list1[i]
# print(list1)
#
# # selection sort descending order
# for i in range(len(list1)):
#     maximum = i
#     for j in range(i+1, len(list1)):
#         if list1[maximum] < list1[j]:
#             maximum = j
#     list1[i], list1[maximum] = list1[maximum], list1[i]
# print(list1)


# bubble sort ascending order
for i in range(len(list1) - 1, 0, -1):
    for j in range(i):
        if list1[j] > list1[j + 1]:
            temp = list1[j]
            list1[j] = list1[j + 1]
            list1[j + 1] = temp
print(list1)

# bubble sort descending order

for i in range(len(list1) - 1, 0, -1):
    for j in range(i):
        if list1[j] < list1[j + 1]:
            temp = list1[j]
            list1[j] = list1[j + 1]
            list1[j + 1] = temp
print(list1)
