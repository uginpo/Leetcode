# 26. Remove Duplicates from Sorted Array
def removeDuplicates(nums: list[int]) -> int:
    length = len(nums)
    temp = sorted(list(set(nums)))
    nums.clear()
    nums.extend(temp)
    nums.extend([9]*(length-len(temp)))
    return len(temp)


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums))
print()
print(nums)
