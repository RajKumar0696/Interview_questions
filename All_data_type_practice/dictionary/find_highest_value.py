def get_highest_value(given_dict):
    list_of_keys = list(given_dict.keys())
    maximum = given_dict[list_of_keys[0]]
    new_dict = {}
    for key in range(len(list_of_keys)):
        if given_dict[list_of_keys[key]] > maximum:
            maximum = given_dict[list_of_keys[key]]
            new_dict.update({list_of_keys[key]: maximum})
    return new_dict


my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
first = get_highest_value(my_dict)
print(first)