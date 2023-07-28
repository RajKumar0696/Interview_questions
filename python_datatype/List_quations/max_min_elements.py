arr = [1, 2, 3, 4, 5]
print(max(arr))
print(min(arr))

maximum = arr[0]
length = len(arr)
for i in range(1, length):
    if arr[i] > maximum:
        maximum = arr[i]
print("max is:", maximum)


minimum = arr[0]
length = len(arr)
for i in range(1, length):
    if arr[i] < minimum:
        minimum = arr[i]
print("min is", minimum)
