list1 = [5, 3, 4, 5, 67, 7]
for i in range(len(list1)):
    print(i, list1[i])
# 0 5
# 1 3
# 2 4
# 3 5
# 4 67
# 5 7

# find the index of given list
list1 = [5, 3, 4, 5, 67, 7]
number = int(input("Enter number:"))
count = 0
for i in range(len(list1)):
    if list1[i] == number:
        count = count + 1
        print(i, list1[i])

if count == 0:
    print("given number not in list")


# s = ['a', 'b', 'c', 'd']
# print(type(s))
# s1 = ''
# for i in s:
#     s1 = s1 + i
# print(s1)
# print(type(s1))


# <class 'list'>
# abcd
# <class 'str'>
