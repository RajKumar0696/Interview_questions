list1 = [1, 2, 3, 4, 5]
list2 = [ 7, 8, 9]
count = 0
for i in list1:
    for j in list2:
        if i == j:
            count = count + 1
if count >= 1:
    print("true")
else:
    print("false")


