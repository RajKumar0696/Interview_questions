# Exercise 6: Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

for key_item in keys:
    sample_dict.pop(key_item)
print(sample_dict)

# # Exercise 7: Check if a value exists in a dictionary
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# user_value = int(input("Enter value:"))
# if user_value in sample_dict.values():
#     print("Yes")
# else:
#     print("No")

# Exercise 8: Rename key of a dictionary
# Write a program to rename a key "city" to a "location" in the following dictionary.
# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
#
# key = input("Enter your key:")
# change_key = input("Enter your key:")
# sample_dict[change_key] = sample_dict.pop(key)
# print(sample_dict)

# Exercise 9: Get the key of a minimum value from the following dictionary
sample_dict = {
    'Physics': 82,
    'Math': 65,
    'History': 75
}

print(min(sample_dict.items()))

# Exercise 10: Change value of a key in a nested dictionary
# Write a Python program to change Brad’s salary to 8500 in the following dictionary.
sample_dict = {
    'emp1': {'name': 'Jon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict['emp3']['salary'] = 8500
print(sample_dict)
