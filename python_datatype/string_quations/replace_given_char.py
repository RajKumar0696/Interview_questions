string = input("Enter string:")
char = input("Enter string:")
result = ''
for i in string:
    if i == " ":
        i = char
    result = result + i
print(result)
