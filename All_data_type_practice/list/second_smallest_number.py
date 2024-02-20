def get_uniq_numbers(given_list):
    uniq = []
    for i in given_list:
        if i not in uniq:
            uniq.append(i)
    return uniq


def get_smallest_number(given_list):
    minimum = given_list[0]
    for i in range(len(given_list)):
        if given_list[i] < minimum:
            minimum = given_list[i]
    return minimum


list1 = [12, 4, 56, 78, 3, 4, 3, 78, 45]
uniq_list = get_uniq_numbers(list1)
first_min = get_smallest_number(uniq_list)
print(first_min)
uniq_list.remove(first_min)
second_min = get_smallest_number(uniq_list)
print(second_min)
