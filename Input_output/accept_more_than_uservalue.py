# Exercise 5: Accept a list of 5 float numbers as an input from the user
list1 = []
for i in range(0, 5):
    enter_num = float(input("Enter your decimal number:"))
    list1.append(enter_num)
print(list1)
print("Total of decimal numbers is:",list1)