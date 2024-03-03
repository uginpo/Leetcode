def trap(height: list[int]) -> int:
    length = len(height)
    left_max = [0]
    right_max = [0]
    l_max = height[0]
    r_max = height[-1]

    left_max.extend([l_max := max(l_max, height[i-1])
                    for i in range(1, len(height))])

    right_max.extend([r_max := max(r_max, height[i+1])
                      for i in range(len(height)-2, -1, -1)])
    right_max = right_max[::-1]

    water = 0
    for l, r, w in zip(left_max, right_max, height):
        delta = min(l, r) - w
        water += delta if delta > 0 else 0

    print(f'    {height=}')
    print(f'  {left_max=}')
    print(f' {right_max=}')
    return water


height = [0, 1, 0, 1]
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))
