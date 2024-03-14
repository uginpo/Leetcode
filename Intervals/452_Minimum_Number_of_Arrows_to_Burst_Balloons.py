def findMinArrowShots(points: list[list[int]]) -> int:
    N = len(points)
    if N <= 1:
        return N

    points = sorted(points, key=lambda x: x[0])
    print(f'{points=}')

    res = [points[0]]

    for i in range(1, N):
        current_interval = points[i]
        common_interval = res[-1]

        r_common = common_interval[1]

        l_current = current_interval[0]
        r_current = current_interval[1]

        match (l_current - r_common) <= 0:
            case True:
                left = l_current
                right = min(r_common, r_current)
                res[-1] = [left, right]
            case False:
                # no common element
                res.append(current_interval)

    print(res)
    return len(res)


points = [[10, 16], [2, 8], [1, 6], [7, 12]]
points = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(findMinArrowShots(points))
