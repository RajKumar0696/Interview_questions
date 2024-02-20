a = int(input("Enter num"))
b = int(input("Enter num"))
c = int(input("Enter num"))

numbers = a, b, c
minimum = numbers[0]
for i in range(len(numbers)):
    if numbers[i] < minimum:
        minimum = numbers[i]
print(minimum)

if a <= b and a <= c:
    print("a", a)
if b <= a and b <= c:
    print("b", b)
if c <= a and c <= b:
    print("c", c)
