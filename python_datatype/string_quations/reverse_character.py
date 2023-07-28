string = 'My Name is Jessa'
words = string.split()
tot = []
for i in words:
    tot.append(i[::-1])
total = " ".join(tot)
print(total)
