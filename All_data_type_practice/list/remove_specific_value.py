# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
index = [0, 4, 5]
new_list = []
for i in range(len(sample_list)):
    if i not in index:
        new_list.append(sample_list[i])
print(new_list)
