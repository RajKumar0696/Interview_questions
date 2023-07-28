list1 = [12, 46, 46, 12, 48, 46, 76, 54, 12]
num = int(input("Enter number:"))
count = 0
for i in list1:
    if i == num:
        count = count + 1
print("Total ", num, "occurrences is:", count)


list2 = list1.count(num)
print(list2)