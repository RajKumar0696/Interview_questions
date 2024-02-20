l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
new_dict = {}
for i, j in l:
    new_dict.setdefault(i, []).append(j)
print(new_dict)
