# Write a Python program to find all the unique words and count the frequency of occurrence from
# a given list of strings. Use Python set data type.

words = ['Red', 'Green', 'Red', 'Blue', 'Red', 'Red', 'Green']
uniq = []
for i in words:
    if i not in uniq:
        uniq.append(i)
new_dict = {}
for i in uniq:
    count = 0
    for j in words:
        if i == j:
            count += 1
    new_dict.update({i: count})
print(new_dict)


def word_count(words):
    word_set = set(words)
    word_counts = {}
    for word in word_set:
        word_counts[word] = words.count(word)
    return word_counts


word = ['Red', 'Green', 'Red', 'Blue', 'Red', 'Red', 'Green']
print(word_count(word))
