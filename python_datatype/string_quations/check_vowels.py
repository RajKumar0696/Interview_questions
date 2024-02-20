# # check count of vowels
# string = input("Enter your string:")
# low = string.lower()
# count = 0
# for i in string:
#     if i == 'a' or i == "e" or i == "i" or i == 'o' or i == 'u':
#         count = count + 1
# print(count)
#
# # print vowels letters along with occurrence
# vowels = "aeiou"
# for vow in vowels:
#     count = 0
#     for str in string:
#         if vow == str:
#             count = count + 1
#     print(vow, count)

# check given character vowel or not
string = input("Enter your string:")
low = string.lower()
if string == 'a' or string == "e" or string == "i" or string == 'o' or string == 'u':
    print("yes", string)
else:
    print("no", string)
