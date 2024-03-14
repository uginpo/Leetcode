def summaryRanges(nums: list[int]) -> list[str]:
    result = []
    l = r = 0
    N = len(nums)

    for i in range(1, N):
        if nums[i] - nums[l] == i-l:
            r = i

        else:
            if l == r:
                result.append(str(nums[l]))
            else:
                result.append(f'{nums[l]}->{nums[r]}')

            l = r = i

        if i == N-1:
            if l != r:
                result.append(f'{nums[l]}->{nums[r]}')
            else:
                result.append(str(nums[i]))

    return result


nums = [0, 1, 2, 4, 5, 7]
nums = [0, 2, 3, 4, 6, 8, 9]
# Output: ["0","2->4","6","8->9"]
nums = [0, 7]
print(summaryRanges(nums))
