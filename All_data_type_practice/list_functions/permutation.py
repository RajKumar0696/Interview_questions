def permutations(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]
    result = []
    for i in range(len(nums)):
        m = nums[i]
        rem_list = nums[:i] + nums[i+1:]
        for j in permutations(rem_list):
            result.append([m] + j)
    return result



list1 = [1, 2, 3]
print(permutations(list1))
