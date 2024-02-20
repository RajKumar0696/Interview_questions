string = input("Enter string:")
even = string[0::2]
print(even)
odd = string[1::2]
print(odd)
even = ""
odd = ""
for i in range(len(string)):
    if i % 2 == 0:
        even = even + string[i]
    else:
        odd = odd + string[i]
print(even)
print(odd)
