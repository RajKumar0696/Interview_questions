number = [2,1, 3, 5, 7, 11, 13]
list1 = []
for i in number:
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count = count + 1
    if count == 2:
        list1.append("prime")
    else:
        list1.append("no")


for i in list1:
    if i == "no":
        print("false")
        break
    else:
        print("true")


