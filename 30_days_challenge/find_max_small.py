# qus: get the numbers of int from user and find max and min
list1 = []
number = ""
print("Press 0 to exit")
while number != 0:
    number = int(input("Enter number: "))
    if number != 0:
        list1.append(number)
print(max(list1))
print(min(list1))


