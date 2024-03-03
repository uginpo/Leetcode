def twoSum(numbers: list[int], target: int) -> list[int]:
    N = len(numbers)
    l = 0
    r = N-1
    while l != r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l+1, r+1]
        elif s < target:
            l += 1
        elif s > target:
            r -= 1

    return numbers


numbers = [2, 7, 11, 15]
target = 9
numbers = [-1, 0]
target = -1
print(twoSum(numbers, target))
