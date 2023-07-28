# swap first and last number in given list
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
# print(list1)
# l1 = list1[0]
# list1[0] = list1[-1]
# list1[-1] = l1
# print(list1)
#
# # without variable
# list1[0], list1[-1] = list1[-1], list1[0]
#
# print(list1)

for i in list1[::-1]:
    print(i, end="")
