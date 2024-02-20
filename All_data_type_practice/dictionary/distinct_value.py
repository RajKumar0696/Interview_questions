L = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
     {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
duplicate = []
original = []
for items in L:
    for val in items.values():
        if val not in original:
            original.append(val)
        else:
            duplicate.append(val)
print(original)
