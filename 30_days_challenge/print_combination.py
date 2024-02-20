# qus: Print combination of a,b,c not repeating
from itertools import permutations, combinations
value = ["a", "b", "c"]
single = list(permutations(value, 1))
double = list(permutations(value, 2))
triple = list(permutations(value, 3))
for i in single:
    print(" ".join(i))
for i in double:
    print(" ".join(i))
for i in triple:
    print(" ".join(i))

# second way
for i in range(1, 4):
    for combo in permutations(value, i):
        print(" ".join(combo))
