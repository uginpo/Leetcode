def maxArea(height: list[int]) -> int:
    N = len(height)
    l = 0
    r = N-1
    water = 0
    while l != r:
        water = max(water, min(height[l], height[r])*(r-l))
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
    return water


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# output =49
print(maxArea(height))
