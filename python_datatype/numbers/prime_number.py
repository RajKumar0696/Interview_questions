# To check given number is prime or not
number = int(input("Enter number:"))
count = 0
for i in range(1, number + 1):
    if number % i == 0:
        count = count + 1
if count == 2:
    print("given number is  prime")
else:
    print("given number is not prime")

# print range of prime numbers

for i in range(2, number+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
