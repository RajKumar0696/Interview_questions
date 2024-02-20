number = 987654321

sum_of = 0

while number != 0 :
    digit = number % 10
    sum_of = sum_of + digit
    number = number // 10
print(sum_of)