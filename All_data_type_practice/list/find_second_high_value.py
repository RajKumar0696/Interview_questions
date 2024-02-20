def get_uniq_value(given_list2):
    if len(given_list2) > 2:
        uniq = []
        for i in given_list2:
            if i not in uniq:
                uniq.append(i)
        return uniq


def get_max_number(given_list):
    maximum = given_list[0]
    for i in range(len(given_list)):
        if given_list[i] > maximum:
            maximum = given_list[i]
    return maximum


list1 = [12, 4, 56, 78, 3, 79, 79, 78, 45]
uniq_list = get_uniq_value(list1)
first_max = get_max_number(uniq_list)
uniq_list.remove(first_max)
sec_max = get_max_number(uniq_list)
uniq_list.remove(sec_max)
third_max = get_max_number(uniq_list)
print("sec_max :", sec_max)
print(third_max)