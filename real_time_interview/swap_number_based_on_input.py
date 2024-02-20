list1 = [1, 2, 3, 4, 5, 6, 7, 8]
num = int(input("Enter number: "))

for i in range(num):
    list1.append(list1[0])
    list1.remove(list1[0])

print(list1)
