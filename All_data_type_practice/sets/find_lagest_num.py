def largest_num(nums):
    new_set = set(nums)
    if len(nums) < 3:
        return None
    list1 = list(new_set)
    list1.sort(reverse=True)
    print(list1)
    return list1[2]


list2 = [1, 1, 2, 3, 4, 5, 4, 3, 2, 1, 4, 6, 6, 9]
print(largest_num(list2))
