number = int(input("Enter how many times you want :"))
number2 = int(input("Enter which table you want:"))

for i in range(1, number + 1):
    print(i, "*", number2, "=", i * number2)


# a) either one is 6
#
# b) or if their sum is 6
#
# c) or the difference is 6
number = int(input("Enter the number:"))
number2 = int(input("Enter which table you want:"))

if number == 6 or number2 == 6 or number + number2 == 0 or abs(number-number2) == 6:
    assert True

