# qus: Print range of 100 numbers but not print 77 86 33

number = 100
for i in range(1, number+1):
    if i == 33 or i == 77 or i == 86:
        continue
    print(i, end=" ")