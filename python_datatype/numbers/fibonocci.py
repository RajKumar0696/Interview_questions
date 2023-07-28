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

fact = 1
for i in range(1, number+1):
    fact = fact * i
print(fact)


for i in range(2, number+1):

    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
count= 0
for i in range(1,number+1):
    if number%i == 0:
        count= count+1
if count == 2:
    print("prime")
else:
    print("not")