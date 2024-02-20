str1 = "python is a programming language"
uniq_letters = ""

for i in str1:
    if i not in uniq_letters:
        uniq_letters += i

for i in uniq_letters:
    count = 0
    for j in str1:
        if i == j:
            count += 1
    print(i, count)