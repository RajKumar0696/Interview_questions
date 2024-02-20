list1 = ["abc", "bcc", "abc", "acc", "bcc", "abc"]
uniqs = []
for list1_item in list1:
    if list1_item not in uniqs:
        uniqs.append(list1_item)
print(uniqs)

for uniq_item in uniqs:
    count = 0
    for list1_item in list1:
        if uniq_item == list1_item:
            count += 1
    print(uniq_item, "is occurred",count,"times")




