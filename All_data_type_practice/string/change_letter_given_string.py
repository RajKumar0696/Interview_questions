# 4. Write a Python program to get a string from a given string where all occurrences of
# its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

string = "rajkumar"
print(string[1::])
first = string[0]
str1 = string.replace(first, "$")
str1 = first + str1[1::]
print(str1)


for letter in string[::-1]:
    if letter == first:
        string = string.replace(letter, "$")
        string = first + string[1::]
print(string)
