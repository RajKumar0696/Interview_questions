number = int(input("Enter number:"))
new_dict = {}
for i in range(1, number+1):
    new_dict.update({i: i*i})
print(new_dict)

sum_of = 0
for i in new_dict:
    sum_of = sum_of + new_dict[i]
print(sum_of)