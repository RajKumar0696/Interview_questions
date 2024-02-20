ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
new_dict = {value: key for key, value in ascii_dict.items()}
new = {value: key for key, value in new_dict.items()}
print(new_dict)
print(new)
print(ascii_dict['A'])

new_dict = {value: key for key, value in ascii_dict.items()}
