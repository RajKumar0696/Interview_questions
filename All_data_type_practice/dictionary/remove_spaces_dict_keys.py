student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
list1 = list(student_list.keys())
print(list1)
empty = []
key = []
new_dict = {}
for i in list1:
    for j in i:
        if j == " ":
            empty.append(j)
        else:
            key.extend(j)
print(empty)
print(key)
result = " ".join(key)
print(result)

student_dict = {x.translate({32: None}): y for x, y in student_list.items()}
print(student_dict)