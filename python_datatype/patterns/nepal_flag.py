def tryangle(rows):
    for i in range(rows):
        for j in range(i + 1):
            print("* ", end="")
        print("\r")


def line(rows):
    for i in range(rows):
        print("*")


rows = int(input("Enter your rows number:"))
tryangle(rows)
tryangle(rows)
line(rows)

