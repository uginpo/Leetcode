def productExceptSelf(nums: list[int]) -> list[int]:
    zero_ind = []
    product = 1
    for ind, num in enumerate(nums):
        if num == 0:
            zero_ind.append(ind)
        else:
            product *= num
    match len(zero_ind):
        case 0:
            return [product//i for i in nums]
        case 1:
            res = [0]*len(nums)
            res[zero_ind[0]] = product
            return res
        case _:
            return [0]*len(nums)


nums = [1, 2, 3, 4]
nums = [-1, 1, 0, -3, 3, 0]
nums = [-1, 1, 0, -3, 3]
print(productExceptSelf(nums))

# [24,12,8,6]
# [0,0,9,0,0]
