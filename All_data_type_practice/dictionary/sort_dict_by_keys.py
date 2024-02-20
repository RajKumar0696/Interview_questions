color_dict = {'red': '#FF0000',
              'green': '#008000',
              'black': '#000000',
              'white': '#FFFFFF'}

sorted_ = sorted(color_dict.keys(), reverse=False)
new_dict = {}
for i in sorted_:
    new_dict.update({i: color_dict[i]})
print(new_dict)
