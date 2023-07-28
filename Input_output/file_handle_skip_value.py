# Exercise 6: Write all content of a given file into a new file by skipping line number 5
# line1
# line2
# line3
# line4
# line5
# line6
# line7

with open("new_file.txt", 'r') as file:
    data = file.read().replace("\n", "")
print(data)

