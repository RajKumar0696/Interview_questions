mylist = ["geeks", "for", "geeks"]
length = (len(mylist))
for i in range(length+1):
    print(i)
    if i == length:
        del mylist[i-1]
print(mylist)

reverse = []
for i in mylist:
    reverse.append(i[::-1])
data = " ".join(reverse)
print(data)
