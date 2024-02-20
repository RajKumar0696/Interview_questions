new_dict = {"raj": 27, "hema": 26, "mithansh": 2, "hanisha": 3}
keys = list(new_dict.values())
for i in range(len(keys)):
    maximum = i
    for j in range(i+1, len(keys)):
        if keys[maximum] > keys[j]:
            maximum = j
    keys[i], keys[maximum] = keys[maximum], keys[i]

print(keys)

sorted_ = sorted(new_dict.values(), reverse=False)
print(sorted_)


