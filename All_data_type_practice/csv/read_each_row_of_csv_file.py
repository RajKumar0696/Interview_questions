import csv
value = [['user', 'Password', 'exp'],
         ['admin@yourstore.com', 'admin', 'Pass'],
         ['admistore.com', 'admin', 'Fail'],
         ['admin@yourstore.com', 'adm', 'Fail'],
         ['admin@yourst.com', 'aadmin', 'Fail']]
with open("sample.csv", "w") as file:
    data = csv.writer(file)
    for row in value:
        data.writerow(row)
with open("sample.csv", "r") as file:
    print(file.read())
