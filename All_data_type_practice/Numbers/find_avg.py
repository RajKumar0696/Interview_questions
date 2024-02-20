number = int(input("Enter your number: "))
sum_of = 0
for i in range(number):
    values = int(input("Enter your number: "))
    sum_of = sum_of + values
avg = sum_of / number
print(avg)