sentence = "Python is a programming language. This is a beginner language. This is a snake language"
split = sentence.split()
uniq = []
for i in split:
    if i not in uniq:
        uniq.append(i)
new_dict = {}
for i in uniq:
    count = 0
    for j in split:
        if i == j:
            count = count + 1
            new_dict.update({i:count})
print(new_dict)
