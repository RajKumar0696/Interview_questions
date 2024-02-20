# qus: Put the value in list what are jobs available based on python. after delete/remove one by one in list.
# last print your domain only

list1 = ["data analyst", "developer", "data science", "Automation tester"]
list2 = ["data analyst", "Automation tester"]
list3 = []
for i in list1:
    for j in list2:
        if i == j:
            list3.append(list1)
        else:
            list1.pop(0)

print(list1)

