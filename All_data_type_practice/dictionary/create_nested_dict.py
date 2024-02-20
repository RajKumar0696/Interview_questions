num_list = [1, 2, 3, 4]
# expected_res = {1: {2: {3: {4: {}}}}}
new_dict1 = new_dict = {}
for i in num_list:
    new_dict[i] = {}
    new_dict = new_dict[i]
print(new_dict1)
