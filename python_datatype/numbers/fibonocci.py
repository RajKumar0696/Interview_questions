number = int(input("Enter number:"))
n1 = 0
n2 = 1
print(n1)
print(n2)
for i in range(2, number + 1):
    fibonacci = n1 + n2
    print(fibonacci)
    n1 = n2
    n2 = fibonacci


n1 = 0
n2 = 1
print(n1)
print(n2)
for i in range(2, number+1):
    febb = n1 + n2
    print(febb)
    n1 = n2
    n2 = febb
