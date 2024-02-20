sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
vals = list(sample_dict.values())
maximum = vals[0]
max_index = 0
for i in range(len(vals)):
    if vals[i] > maximum:
        maximum = vals[i]
        max_index = i
print(list(sample_dict)[max_index], maximum)
