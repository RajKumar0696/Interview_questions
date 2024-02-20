str1 = 'w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
uniq = ''
new_dict = {}
for i in str1:
    if i not in uniq:
        uniq = uniq + i
for i in uniq:
    count = 0
    for j in str1:
        if i == j:
            count = count + 1
            new_dict.update({i: count})
print(new_dict)
