myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
given_key = input("Enter key:")
if given_key in myDict.keys():
    # del myDict[given_key]
    myDict.pop(given_key)
print(myDict)
