from collections import defaultdict


def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    nums_dict = defaultdict(list)

    for ind, num in enumerate(nums):
        if num in nums_dict:
            if abs(ind - nums_dict[num][-1]) <= k:
                return True
        nums_dict[num].append(ind)

    return False


nums = [1, 2, 3, 1]
k = 3
nums = [1, 0, 1, 1]
k = 1

print(containsNearbyDuplicate(nums, k))
