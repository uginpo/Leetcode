def trap(height: list[int]) -> int:
    length = len(height)
    l = 0
    r = length - 1
    maxL = height[0]
    maxR = height[-1]
    water = 0
    waters = []

    while l <= r:
        match maxL - maxR <= 0:
            case True:
                delta = maxL - height[l]
                water += delta if delta > 0 else 0
                maxL = max(maxL, height[l])
                l += 1
            case False:
                delta = maxR - height[r]
                water += delta if delta > 0 else 0
                maxR = max(maxR, height[r])
                r -= 1
        waters.append(delta)

    print(f'{height=}')
    print(f'{waters=}')
    return water


height = [0, 1, 0, 1]
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height = [5, 5, 1, 7, 1, 1, 5, 2, 7, 6]
print(trap(height))
