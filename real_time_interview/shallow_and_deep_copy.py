# Shallow copy
"""A shallow copy creates a new object but does not
create copies of nested objects within the original object.
 Instead, it copies references to the nested objects. If the nested objects are mutable,
  changes made to them will be reflected in both the original and the copied objects.

In Python, you can create a shallow copy using the copy module or by using
the copy() method of the object."""

import copy

list1 = [1, 2, [3, 4], 5, 6]
shallow_copy = copy.copy(list1)

shallow_copy[2][0] = "r"
print(list1)
print(shallow_copy)


# deep copy
"""A deep copy, on the other hand, creates a new object and recursively copies all nested objects within the 
original object. Changes made to nested objects in the copy do not affect the original object, and vice versa.

You can create a deep copy using the copy module."""
list1 = [1, 2, [3, 4], 5, 6]

deep_copy = copy.deepcopy(list1)

deep_copy[2][0] = "h"
print(list1)
print(deep_copy)