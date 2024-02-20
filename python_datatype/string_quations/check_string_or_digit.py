value = input("Enter value:")
for i in value:
    if '0' <= i <= '9':
        print("digit", i)
    else:
        print("character", i)
        