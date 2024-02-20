# count given element
tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7
print(tuplex.count(4))


# Write a Python program to check whether an element exists within a tuple.
tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
given_str = input("Enter your value:")
for i in tuplex:
    if i == given_str:
        print("yes")
        break
    else:
        print("no")

print(given_str in tuplex)
print(given_str not in tuplex)


# convert list to tuple
list1 = [5, 10, 7, 4, 15, 3]
tup1 = tuple(list1)
print(tup1)
