string = "google.com"
uniqs = ""
for letter in string:
    if letter not in uniqs:
        uniqs = uniqs + letter
total = {}
for uniq in uniqs:
    count = 0
    for letter in string:
        if uniq == letter:
            count = count + 1
            total.update({uniq: count})
print(total)
