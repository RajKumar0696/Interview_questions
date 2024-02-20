string = input("Enter your string: ")
last = ''
for i in string[len(string)-4:]:
    last = i + last
print(last)

rev = "".join(reversed(string[-4:]))
print(rev)
