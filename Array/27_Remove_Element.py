def removeElement(nums: list[int], val: int) -> int:
    back_ind = len(nums)-1
    count = 0
    for i in range(len(nums)-1, -1, -1):
        if nums[i] == val:
            if i != back_ind:
                nums[i], nums[back_ind] = nums[back_ind], nums[i]
            count += 1
            back_ind -= 1
    return len(nums) - count


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2


def removeElement_fast(nums: list[int], val: int) -> int:
    length = len(nums)
    temp = [i for i in nums if i != val]
    nums.clear()
    nums.extend(temp)
    nums.extend([val]*(length-len(temp)))
    return len(temp)


print(removeElement_fast(nums, val))
print()
print(nums)
