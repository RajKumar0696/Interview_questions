# 54321
# 5432*
# 543**
# 54***
# 5****
# *****
number = 5
for i in range(1,number+2):
    for j in range(number,0,-1):
        if i<=j:
            print(j,end="")

        else:
            print("*",end="")
    print("\r")

