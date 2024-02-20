def palindrome(given_list):
    return given_list == given_list[::-1]


list1 = [1, 2, 3, 2]

print(palindrome(list1))
