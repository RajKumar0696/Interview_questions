"""Counter is a built-in data structure which is used to count the occurrence of each
value present in an array or list.

The following code is counting the number of occurrences of the value 2 in the given list."""

from collections import Counter

list1 = [1, 2, 3, 4, 3, 2, 4, 5, 6, 3, 4, 4]
result = Counter(list1)
print(result[4])