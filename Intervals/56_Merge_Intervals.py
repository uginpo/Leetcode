def merge(intervals: list[list[int]]) -> list[list[int]]:
    N = len(intervals)
    if N <= 1:
        return intervals

    intervals = sorted(intervals, key=lambda x: x[0])
    print(f'{intervals=}')

    res = [intervals[0]]

    for i in range(1, N):
        current_interval = intervals[i]
        merged_interval = res[-1]

        left = min(current_interval[0], merged_interval[0])
        left_second = max(current_interval[0], merged_interval[0])

        right = max((current_interval[1], merged_interval[1]))
        right_second = min((current_interval[1], merged_interval[1]))

        if left_second <= right_second:
            res[-1] = [left, right]
        else:
            res.append([left_second, right])

    return res


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# Output: [[1,6],[8,10],[15,18]]

intervals = [[1, 4], [0, 0]]

print(merge(intervals))
