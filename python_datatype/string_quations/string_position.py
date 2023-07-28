def finding(name):
    finding_cha = input("Enter the character:")
    if finding_cha in name :
        return True
    # if name.index(finding_cha) == 0 or name.index(finding_cha) == 1:
    #     return True
    else:
        return False


name = input("Enter name:")
print(finding(name))
