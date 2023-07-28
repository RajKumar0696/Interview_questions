actual = "Name", "Is", "James"
# exp = Name**Is**James

print("Name", "Is", "James", sep="**")
for word in actual:
    print(word + "**", end="")

#  Convert Decimal number to octal using print() output formatting
num = 10
print('%o' % num)
