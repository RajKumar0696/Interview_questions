# qus: number of line paragraph. find length of letters, length of words and occurrence of letters

str1 = "It's advisable to check the official Selenium documentation and release notes for the most " \
       "up-to-date information on the changes and improvements introduced in Selenium " \
       "4. Additionally, if you're working with Selenium, it's a good practice to use the " \
       "latest stable version to take advantage of new features and improvements."
print("Length of str1 is: ", len(str1))
words = str1.split()
print("Length of words:", len(words))
str2 = []
for i in words:
    if i not in str2:
        if i != " ":
            str2.append(i)

for i in str2:
    count = 0
    for j in words:
        if i == j:
            count = count + 1
    print(i, count)
