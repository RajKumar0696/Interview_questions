price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
rever = reversed(price)
print(list(rever))

# Write a Python program to count the elements in a list until an element is a tuple.
num = [10, 20, 30, (10, 20), 40]
count = 0
for i in num:
    print(type(i))
    if isinstance(i, tuple):
        break
    count += 1
print(count)

# method 2
count = 0
for i in num:
    if type(i) == type((10, 20)):
        break
    count += 1
print(count)
