x = {"s1": {"p1": 42, "p2": 90, "p3": "python"},
     "s2": {"q1": 32, "q2": 100, "q3": 70},
     "s3": {"s1": 20, "s2": 40, "s3": 70}}
val1 = x["s1"].values()
print(list(val1))
add = 0
for i in val1:
    if type(i) == int:
        add = add + i
print(add)
val2 = x["s2"].values()
print(list(val2))
print(sum(val2))
val3 = x["s3"].values()
print(list(val3))
print(sum(val3))