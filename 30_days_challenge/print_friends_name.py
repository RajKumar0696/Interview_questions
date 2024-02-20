# qus: get friends name from users and print all names in same line
# along with add we are all to gather and spread love
print("Hey, enter q to exit:")
msg = ''
str1 = ""
while str1 != 'q':
    str1 = input('Enter:')
    if str1 == 'q':
        msg = msg + "we are all together forever!!!"
    else:
        msg = str1 + "," + msg
print(msg)
