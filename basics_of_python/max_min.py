arr = [1, 2, 33, 4, 5]
print(min(arr))
print(max(arr))

maximum = arr[0]
length = len(arr)
for i in range(length):
    if arr[i] > maximum:
        maximum = arr[i]
print(maximum)

mylist = ["geeks", "for", "geeks"]
length = len(mylist)
for i in range(length + 1):
    if i == length:
        del mylist[i - 1]
print(mylist)

number = 100
for i in range(number + 1):
    if i > 0:

        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print("The prime number is:", i)

str1 = "Welcome to python programming"
words = str1.split(" ")
print(words)
words = words[::-1]
print(words)


string = "Welcome to python programming"
sub_string = "python"

if sub_string in string:
    print("string found")
else:
    print("Not found")
