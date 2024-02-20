"""OrderedDict is a dictionary that ensures its order is maintained. For exampl,
if the keys are inserted in a specific order, then the order is maintained.
 Even if you change the value of the key later, the position will remain the same."""

from collections import OrderedDict
order = OrderedDict()
order['a'] = 1
order['b'] = 2
order['c'] = 3
print(order)

#unordered dictionary
unordered=dict()
unordered['a'] = 1
unordered['b'] = 2
unordered['c'] = 3
print("Default dictionary", unordered)