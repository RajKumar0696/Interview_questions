string = input("Enter your string:")
print(string)
index_val = int(input("Enter your index:"))
for char in range(len(string)):
    if char == index_val:
        string = string.replace(string[char], "")
print(string)

# C:\Users\WELCOME\AppData\Local\Programs\Python\Python311\python.exe
# C:\Users\WELCOME\Desktop\Interview_questions\All_data_type_practice\string\remove_nth_char.py
