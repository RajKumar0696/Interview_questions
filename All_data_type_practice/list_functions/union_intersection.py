def union_intersection(list1, list2):
    union = list(set(list1) | set(list2))
    intersection = list(set(list1) & set(list2))
    return union, intersection


l1 = [1, 2, 3, 4, 5, 6]
l2 = [1, 2, 3, 4, 8, 9, 6]
print(union_intersection(l1, l2))
