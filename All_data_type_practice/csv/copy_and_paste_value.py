import csv

with open("sample.csv", "r") as file:
    data = csv.reader(file)
    value = list(data)

with open("new.csv", "w") as file1:
    data = csv.writer(file1)
    data.writerows(value)
# with open("new.csv", "r", newline="" ) as file2:
#     print(csv.reader(file2))
#
with open("sample.csv", "r") as file:
    print(file.read())



