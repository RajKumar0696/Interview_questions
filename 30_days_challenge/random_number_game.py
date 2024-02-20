# qus: first print 1 to 10 random number. Get the number from user. Both is matched print msg

import random
number = random.randint(1, 10)
user_num = int(input("Enter number: "))
print("random number: ", number)
if number == user_num:
    print("Your win")
else:
    print("Sorry please try again latter")
