def threeSum(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)

    if nums[0] == 0 or nums[-1] == 0:
        if nums.count(0) < 3:
            return []
        else:
            return [[0, 0, 0]]
    elif nums[0] > 0 or nums[-1] < 0:
        return []

    N = len(nums)
    print(f'{nums=}')
    triples = []
    f = 0

    while nums[f] <= 0:
        first = nums[f]
        l = f + 1
        r = N - 1

        while l != r:
            res = first + nums[l] + nums[r]
            res = res if res == 0 else res//abs(res)
            match res:
                case 0:
                    a = [first, nums[l], nums[r]]
                    if a not in triples:
                        triples.append(a)
                    l += 1
                case -1:
                    l += 1
                case 1:
                    r -= 1
        f += 1

    return triples


nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1,-1,2],[-1,0,1]]
nums = [1, 1, -2]
nums = [1, 1, 1]
nums = [-1, 0, 1, 0]
nums = [1, 2, -2, -1]
nums = [0, 0, 0]
nums = [-1, -1, -1]
nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
# [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
nums = [-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0]
# [[-5,1,4],[-4,0,4],[-4,1,3],[-2,-2,4],[-2,1,1],[0,0,0]]
print(threeSum(nums))
