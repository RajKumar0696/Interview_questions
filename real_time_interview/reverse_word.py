string = "I Love India"
word = string.split()
reverse = ""
for i in word:
    reverse = i + reverse
result = "".join(reverse)
print(result)

rever = word[::-1]
res = " ".join(rever)
print(res)
