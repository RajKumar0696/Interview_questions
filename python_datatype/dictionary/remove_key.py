myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key = input("Enter key:")
if key in myDict:
    del myDict[key]
print(myDict)