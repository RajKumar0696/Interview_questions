# qus: get travelling areas from user and order alphabetic
str1 = ""
list1 = []
print("press q to exit")
while str1 != "q":
    str1 = input("Enter: ")
    if str1 != "q":
        list1.append(str1)
list1.sort()
print(list1)

