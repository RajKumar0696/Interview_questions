num = int(input("please give a number: "))
sum_of = 0
for i in range(1, (num//2) +1):
    remainder = num % i
    if remainder == 0:
        sum_of = sum_of + i
if sum_of == num:
    print("perfect number")
else:
    print("not perfect")
# perfect number 1 to 1000 is 6 ,28, 496

