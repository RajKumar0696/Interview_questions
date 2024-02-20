list1 = []
if not list1:
    print("emp")


for i in range(5):
    value = int(input("enter number:"))
    list1.append(value)
print(list1)
if len(list1) < 1:
    print("empty")
else:
    print("not empty")
