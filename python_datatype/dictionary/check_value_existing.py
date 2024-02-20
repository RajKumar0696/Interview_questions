sample_dict = {'a': 100, 'b': 200, 'c': 300}
value = int(input("Enter your value:"))
for sample_dict_value in sample_dict.values():
    if value == sample_dict_value:
        print("given value is matched", sample_dict_value)

if value in sample_dict.values():
    print("yes")
else:
    print("no")

key = input("Enter key:")
for sample_dict_key in sample_dict:
    if key == sample_dict_key:
        print("true")
