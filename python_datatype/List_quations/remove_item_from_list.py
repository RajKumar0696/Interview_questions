# remove grater then 50
number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
n = len(number_list)
i = 0
while i < n:
    if number_list[i] > 50:
        del number_list[i]
        n = n - 1
    else:
        i = i + 1
print(number_list)

# for loop

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(len(number_list) - 1, -1, -1):
    if number_list[i] > 50:
        del number_list[i]
print(number_list)


