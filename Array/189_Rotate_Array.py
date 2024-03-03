def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k if len(nums) > k else k % len(nums)
    temp1 = nums[-k:]
    temp2 = nums[:-k]
    nums.clear()
    nums.extend(temp1)
    nums.extend(temp2)

    print(nums)


nums = [1, 2]
k = 3
aswer = [5, 6, 7, 1, 2, 3, 4]
rotate(nums, k)
