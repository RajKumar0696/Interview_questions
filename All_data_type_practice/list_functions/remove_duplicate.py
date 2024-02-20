def remove_duplicate(list1):
    duplicate = []
    original = []
    for i in list1:
        if i not in original:
            original.append(i)
        else:
            duplicate.append(i)
    return original


given_list = [1, 2, 3, 4, 3, 6, 7, 3, 5, 2, 1]
print(remove_duplicate(given_list))
