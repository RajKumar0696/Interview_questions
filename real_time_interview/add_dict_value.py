dict_1 = {'John': 15, 'Rick': 10, 'Misa' : 12 }
dict_2 = {'Bonnie': 18,'Rick': 20,'Matt' : 16 }
for i in dict_1:
    for j in dict_2:
        if i == j:
            dict_1[i]= dict_1[i]+dict_2[j]
print(dict_1)

