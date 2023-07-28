mylist = ["geeks", "for", "geeks"]
length = (len(mylist))
for i in range(length+1):
    if i == length:
        del mylist[i-1]
print(mylist)

reverse = []
for i in mylist:
    reverse.append(i[::-1])
print(reverse)
