# 3. Write a Python program to get a string made of the first 2 and
# last 2 characters of a given string.
# If the string length is less than 2, return the empty string instead.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String
string = input("Enter your string:")
length = len(string)
if length > 2:
    print(string[0:2] + string[-2:])
elif length == 2:
    str = string + string
    print(str)
elif length == 1:
    print("empty")