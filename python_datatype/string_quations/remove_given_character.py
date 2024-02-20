string = input("Enter str:")
character = input("Enter str:")
result = ''
for i in string:
    if i == character:
        pass
    else:
        result = result + i
print(result)

print(string.replace(character, ""))
