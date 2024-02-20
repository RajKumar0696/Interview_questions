def list_of_number(list1):
    max_number = 0
    ordered_list = []
    for i in list1:
        if i > max_number:
            ordered_list.append(i)
            max_number = i
    return ordered_list


given_list = [1, 2, 3, 4, 5, 2, 1, 5]
print(list_of_number(given_list))

