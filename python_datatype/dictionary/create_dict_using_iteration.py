number = int(input("Enter number:"))
new = {}
for i in range(1, number+1):
    new.update({i: i*i})
print(new)
