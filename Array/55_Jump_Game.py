def canJump(nums: list[int]) -> bool:
    r = len(nums)-1
    for l in range(len(nums)-2, -1, -1):
        r = l if r <= l+nums[l] else r

    return True if r == 0 else False


nums = [2, 3, 1, 1, 4]
nums = [3, 2, 1, 0, 4]

print(canJump(nums))
