def change_index(nums):
    first_index = int(input("Enter index value: "))
    location_index = int(input("Enter index value: "))
    while first_index < location_index:
        nums[first_index], nums[location_index] = nums[location_index], nums[first_index]
        # first_index += 1
        # location_index -= 1
    return nums


list1 = [10, 20, 30, 40, 50, 60, 70, 80]
print(change_index(list1))
