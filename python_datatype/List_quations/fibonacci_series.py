# print fibonacci series below given number (Ex: num=10 // out: 0 1 1 2 3 5 8)
num = int(input("Enter your number:"))
n1 = 0
n2 = 1
if num > 1:
    print(n1)
    while n2 <= num:
        n = n1 + n2
        n1 = n2
        n2 = n
        print(n1)

# print given number of times fibonacci series
num = int(input("Enter number:"))
n1 = 0
n2 = 1
count = 0
if num > 1:
    while count < num:
        print(n1)
        n = n1 + n2
        n1 = n2
        n2 = n
        count = count + 1
