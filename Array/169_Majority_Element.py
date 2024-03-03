# The majority element is the element that appears more than ⌊n / 2⌋ times.

def majorityElement(nums: list[int]) -> int:
    res = list(set(nums))
    for num in res:
        if nums.count(num)>len(nums)//2:
            return num


nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))
print()
print(nums)
