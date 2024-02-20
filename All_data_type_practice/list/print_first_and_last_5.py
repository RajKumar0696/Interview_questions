number = 21
first = []
last = []
for i in range(1, number+1):
    if i <= 5:
        first.append(i*i)
    elif i >= 25:
        last.append(i*i)
print(first, last)


list1 = []
for i in range(1, number+1):
    list1.append(i*i)
first = list1[:5]
last = list1[-5:]
print(first)
print(last)
