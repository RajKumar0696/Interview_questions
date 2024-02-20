list1 = ["raj kumarM", "hema   sree", "mithansh"]
length = {}
for word in list1:
    length.update({len(word): word})
print(max(length), length[max(length)])




