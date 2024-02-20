"""Default-dict is exactly like a dictionary in python.
The only difference is that it does not give an exception/key
error when you try to access the non-existent key.

In the following code, even though the 4th index was not initialized,
the compiler still returns a value, 0,
when we try to access it."""

from collections import defaultdict
nums = defaultdict(int)
nums['one'] = 1
nums['two'] = 2
nums['three'] = 3
print(nums['four'])