import csv

# write value in csv file

value = [['user', 'Password', 'exp'],
         ['admin@yourstore.com', 'admin', 'Pass'],
         ['admistore.com', 'admin', 'Fail'],
         ['admin@yourstore.com', 'adm', 'Fail'],
         ['admin@yourst.com', 'aadmin', 'Fail']]
# if file already have store the value in that file,incase no create the file and store
with open("sample.csv", "w") as file:
    data = csv.writer(file)
    for row in value:
        data.writerow(row)
with open("sample.csv", "r") as file:
    print(file.read())

# read value from file
with open("sample.csv") as file:
    data = csv.reader(file)
    for row in data:
        print(row)
