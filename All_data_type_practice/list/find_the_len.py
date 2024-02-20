sample_list = [" The quick brown fox jumps over the lazy dog "]
word = str(sample_list).split()
new_list = []
for i in word:
    if (len(i)) > 4:
        new_list.append(i)
print(new_list)
