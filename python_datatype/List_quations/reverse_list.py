# Exercise 1: Reverse a list in Python
# slicing
list1 = [100, 200, 300, 400, 500]

list2 = list1[::-1]
print(list2)

# for loop
list2 = []
for i in list1:
    list2 = [i] + list2
print(list2)

# reverse() and reversed() method
list1.reverse()
print(list1)

list1 = [100, 200, 300, 400, 500]

list2 = reversed(list1)
print(list(list2))

list_reverse = []
for i in range(len(list1)):
    list_reverse.append(list1.pop())
print( list_reverse)


# Exercise 5: Iterate both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for i, j in zip(list1, list2[:: -1]):
    # for j in list2[::-1]:
    print(i , j)
