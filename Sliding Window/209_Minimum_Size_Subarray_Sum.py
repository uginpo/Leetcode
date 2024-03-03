def minSubArrayLen(target: int, nums: list[int]) -> int:
    print(nums)
    if nums[0] >= target:
        return 1

    l, r = 0, 0
    N = len(nums)
    min_len = N+1
    wind_sum = nums[0]

    while True:
        match target > wind_sum:
            case True:
                if r == N-1:
                    break
                else:
                    r += 1
                    wind_sum += nums[r]

            case _:
                min_len = min(min_len, r - l + 1)
                if r == N-1 and l == N-1:
                    break
                else:
                    wind_sum -= nums[l]
                    l += 1

    min_len = min_len if min_len != N+1 else 0

    return min_len


target = 4
nums = [1, 4, 4]
target = 15
nums = [1, 2, 3, 4, 5]
target = 11
nums = [1, 1, 1, 1, 1, 1, 1, 1]
target = 7
nums = [2, 3, 1, 2, 4, 3]
print(minSubArrayLen(target, nums))
