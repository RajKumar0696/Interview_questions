item_list = [{'item': 'item1', 'amount': 400},
             {'item': 'item2', 'amount': 300},
             {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300}
from collections import Counter
result = Counter()
for i in item_list:
    result[i['item']] += i['amount']
print(result)


