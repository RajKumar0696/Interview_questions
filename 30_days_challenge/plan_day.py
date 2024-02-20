# qus: Options add,print,remove and exit

str1 = ""
list1 = []
print("enter 'exit' to exit")
while str1 != 'exit':
    print("please select options:1.add, 2.remove, 3.print:")
    str1 = input("Enter: ")
    if str1 == "add":
        str1 = input("Enter your plan: ")
        list1.append(str1)
    elif str1 == "remove":
        list1.clear()
    elif str1 == "print":
        print(list1)


