number = int(input("Enter how many lists you want: "))
dict1 = {}
empty_list1 = []
for i in range(1, number + 1):
    list1 = []
    dict1.update({i: list1})
    empty_list1.append(list1)
dict1[1] = [1, 2, 3, 4, 5]
print(dict1)
print(empty_list1)
