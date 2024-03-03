# 26. Remove Duplicates from Sorted Array

def removeDuplicates(nums: list[int]):
    old = nums[0]
    count = 1
    lenght = 0
    for i in range(1, len(nums)):
        if nums[i] == old:
            count += 1
            if count > 2:
                nums[i] = 100000
                lenght += 1
        else:
            count = 1
            old = nums[i]
    nums.sort()
    return len(nums)-lenght


nums = [1, 1, 1, 2, 2, 3]
print(removeDuplicates(nums))
print()
print(nums)
