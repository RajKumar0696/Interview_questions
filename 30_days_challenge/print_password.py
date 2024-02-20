# qus: generate password without repeating (length 10)

import random
import string


def generate_password():
    number = string.digits
    letter = string.ascii_lowercase
    list1 = set()
    while len(list1) != 10:
        password = random.choice(number + letter)
        list1.add(password)
    result = "".join(list1)
    return result


list1 = []
number = int(input("Enter number: "))
for i in range(number):
    pass_w = generate_password()
    if pass_w not in list1:
        list1.append(pass_w)
        print(pass_w)
