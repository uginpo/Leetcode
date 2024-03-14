from collections import defaultdict


def twoSum(nums: list[int], target: int) -> list[int]:

    nums_dict = defaultdict(int)

    for ind, num in enumerate(nums):
        nums_dict[num] = ind

    nums_dict = dict(sorted(nums_dict.items()))
    print(nums_dict)

    N = len(nums)
    for i in range(N):
        first = nums[i]
        ind = i
        for value, index in nums_dict.items():
            if index != ind:
                if first + value == target:
                    return [ind, index]
    return []


nums = [2, 7, 11, 15]
target = 9
nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))
