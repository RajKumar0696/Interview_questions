dict_data = {'tamil': 76, 'english': 67, 'maths': 99, 'hindi': 100}
maximum = max(dict_data.values())
print(maximum)
maxi = list(dict_data.values())
maximum = []
for i in dict_data:
    for max in maxi:
        if dict_data[i] < max:
            maximum = dict_data[i]

print(maximum)

max_val = 0
max_key = ""
for k, v in dict_data.items():
    if v > max_val:
        max_val = v
        max_key = k
print(max_key)
print(max_val)
