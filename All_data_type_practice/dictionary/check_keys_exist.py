new_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
key = int(input("Enter your key: "))
for i in new_dict:
    if key == i:
        print("yes", i)
    else:
        print("no", key)



