def jump(nums: list[int]) -> int:
    l, r, step = 0, 0, 0
    while r < len(nums)-1:
        farthest = 0
        for i in range(l, r+1):
            farthest = max(farthest, i+nums[i])
        l = r+1
        r = farthest
        step += 1

    return step


nums = [2, 3, 0, 1, 4]
nums = [2, 0, 2, 0, 1]
nums = [2, 3, 1, 1, 4]
print(jump(nums))
