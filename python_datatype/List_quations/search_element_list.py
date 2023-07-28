number = int(input("Enter number:"))
list1 = [1, 4, 6, 7, 9, 56, 4, 7, ]
count = 0
for i in list1:
    if number == i:
        count = 1
        print("Given number founded:", i)
        break
if count == 0:
    print("Given number not in list")
