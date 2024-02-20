word_list = ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take',
             'see', 'come', 'think', 'look', 'want', 'give', 'use', 'find', 'tell', 'ask',
             'work', 'seem', 'feel', 'leave', 'call']
letter = input("Enter first letter:")
list1 = []
for word in word_list:
    for single in word[:1]:
        if single == letter:
            print(word)
            list1.append(word)
print(list1)
