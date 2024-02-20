string = input("Enter str:")
print(string)
new_string_even = string[1::2]
print(new_string_even)

new_string_odd = string[0::2]
print(new_string_odd)
result = ""
for i in range(len(string)):
    if i % 2 != 0:
        result = result + string[i]
print(result)

result = ""
for i in range(len(string)):
    if i % 2 == 0:
        result = result + string[i]
print(result)
