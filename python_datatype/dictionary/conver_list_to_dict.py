keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

new_dict = dict(zip(keys, values))
print(new_dict)

for employee_item in range(len(keys)):
    new_dict.update({keys[employee_item]: values[employee_item]})
print(new_dict)

keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
new_dict1 = {}
for key in range(len(keys)):
    new_dict1.update({keys[key]:values[key]})
print(new_dict1)

# Exercise 2: Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thi': 30, 'Forty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)

# Exercise 3: Print the value of key ‘history’ from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print("the mark is", sampleDict["class"]['student']['marks']['history'])

# Exercise 4: Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
new_dict = {}
for employee_item in employees:
    new_dict.update({employee_item: defaults})
print(new_dict)

# Exercise 5: Create a dictionary by extracting the keys from a given dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
result = {}
for key_item in keys:
    result.update({key_item: sample_dict[key_item]})
print(result)
