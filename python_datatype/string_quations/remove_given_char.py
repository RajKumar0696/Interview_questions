string = input("Enter string:")
# single = input("Enter string:")
single = 'aeiou'
result = ''
for char in string:
    if char in single:
        char = ''
    result = result + char
print(result)