word = input("Enter your word: ")
print(word.istitle())
print(word.isupper())
print(word.islower())

if word.islower() or word.isupper() or word.istitle():
    print("True")
else:
    print("False")

