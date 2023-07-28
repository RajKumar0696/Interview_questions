with open('sample.txt', 'r') as file:
    data = file.read().replace("\n", ' ')
    print(data)
with open ('sample.txt', 'r') as file:
    data = file.read().replace("\n", " ")
    print(data)


with open("sample.txt", "r") as file:
    line = file.readlines()
    print(line[2])