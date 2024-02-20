given_array = ["hello", "world", "pytest"]
list1 = []
for i in range(len(given_array)):
    for j in range(len(given_array[i])):
        if j % 2 == 0:
            list1.append(given_array[i][j].capitalize())
        else:
            list1.append(given_array[i][j])
    list1.append(",")
array = " ".join(list1)
print(array)
