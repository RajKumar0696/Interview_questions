sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80, 80]
list1 = []
duplicate = []
for i in sample_list:
    if i not in list1:
        list1.append(i)
    else:
        duplicate.append(i)
print(duplicate)

num = 5
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print(factorial)

n1, n2 = 0, 1
print(n1)
print(n2)
for i in range(num):
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3

string = "pythom programming language"
dub = ""
act = ""
for letter in string:
    if letter not in act:
        act = act + letter
    else:
        dub = dub + letter
print(act)
print(dub)

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80, 80]
maximum = sample_list[0]
for i in range(len(sample_list)):
    if sample_list[i] > maximum:
        maximum = sample_list[i]
print(maximum)