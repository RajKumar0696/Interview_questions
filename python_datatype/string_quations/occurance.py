string = input("Enter str:")
string2 = input("Enter str:")
count = 0
for i in string:
    if i == string2:
        count = count + 1
print(count)


words = ['aaa', 'bbb', 'ccc', 'aaa', 'ccc', 'aaa']
uniqs = []

for word in words:
    if word not in uniqs:
        uniqs.append(word)
print(uniqs)

for uniq in uniqs:
    count = 0
    for word in words:
        if uniq == word:
            count = count + 1
    print(uniq, "occurred", count)
