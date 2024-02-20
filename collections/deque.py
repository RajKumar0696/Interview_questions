"""Deque is an optimal version of list used for inserting and removing items.
It can add/remove items from either start or the end of the list.

In the following code, z is being added at the end of the given list and g is at the start of the same list."""

from collections import deque

# initialization
list1 = ["a", "b", "c"]
deq = deque(list1)
print(deq)

# insertion
deq.append("z")
deq.appendleft("g")
print(deq)
# removal
deq.pop()
deq.popleft()
print(deq)
