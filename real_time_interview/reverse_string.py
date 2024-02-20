str1 = 'My Name Is Rajkumar'
word = str1.split()
list1 = []
for i in word:
    list1.append(i[::-1])
    str2 = " ".join(list1)
print(str2)

str1 = 'My Name Is Rajkumar'
word = str1.split()
reverse = ""
for i in word:
    for j in i:
        reverse = j + reverse
print(reverse)
