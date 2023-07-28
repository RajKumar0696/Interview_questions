string = input("Enter string:")
sub_string = input("Enter substring:")
print(string.find(sub_string))
if string.find(sub_string) == -1:
    print("given string is not found")
else:
    print("given string is found")

if sub_string in string:
    print("yes", sub_string)
else:
    print("no", sub_string)