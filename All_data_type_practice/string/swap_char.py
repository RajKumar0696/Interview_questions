# 5. Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'
letter1 = input("enter str:")
letter2 = input("enter str:")
new1 = letter1[:2] + letter2[2:]
new2 = letter2[:2] + letter1[2:]
print(new2 + " " + new1)
