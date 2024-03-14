

def longestConsecutive(nums: list[int]) -> int:

    sorted_nums = sorted(set(nums))
    N = len(sorted_nums)
    longest, count = 1, 1
    l = sorted_nums[0]

    print(sorted_nums)
    for i in range(1, N):
        if sorted_nums[i] - l == 1:
            count += 1
            longest = max(longest, count)
        else:
            count = 1

        l = sorted_nums[i]

    return longest


nums = [100, 4, 200, 1, 3, 2]
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
print(longestConsecutive(nums))
