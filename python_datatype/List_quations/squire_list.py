# Exercise 3: Turn every item of a list into its square
numbers = [1, 2, 3, 4, 5, 6, 7]

squire = list(map(lambda x: x * x, numbers))
print(squire)

squire = []
for i in numbers:
    squire.append(i * i)
    # squi = i * i
    # squire.append(squi)
print(squire)

squire = [x * x for x in (numbers)]
squire = [x * x for x in range(1, len(numbers) + 1)]
print(squire)
