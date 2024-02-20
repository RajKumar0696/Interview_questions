tuplex = "w", 3, "r", "s", "o", "u", "r", "c", "e"
new_tup = tuplex[:1] + tuplex[2:]
print(new_tup)

# Write a Python program to convert a tuple to a dictionary.
# {'w': 2, 'r': 3}
tuplex = ((2, "w"), (3, "r"))
print(dict((y, x) for x, y in tuplex))

# Write a Python program to unzip a list of tuples into individual lists.
# [(1, 3, 8), (2, 4, 9)]
l = [(1, 2), (3, 4), (8, 9)]
print(list(zip(*l)))
