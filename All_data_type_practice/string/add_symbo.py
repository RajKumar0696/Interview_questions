# 16. Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}


def add_middle(symbol, word):
    return symbol[:2] + word + symbol[2:]


print(add_middle("[[]]", "RAJ"))


symbol = "[[]]"
word = "RAJ"
result = symbol[:2] + word + symbol[2:]
print(result)
