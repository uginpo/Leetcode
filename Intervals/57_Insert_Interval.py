def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

    N = len(intervals)
    if N < 1:
        return [newInterval]

    l_new = newInterval[0]
    r_new = newInterval[1]

    if r_new <= intervals[0][0] or l_new <= intervals[0][0]:
        intervals.insert(0, newInterval)
        ind = 0

    elif l_new >= intervals[-1][0]:
        intervals.append(newInterval)
        ind = N-1

    else:
        for i in range(1, len(intervals)):
            l_prev = intervals[i-1][0]
            l_next = intervals[i][0]

            if l_prev <= l_new <= l_next:
                intervals.insert(i, newInterval)
                ind = i-1
                break
    N += 1

    res = intervals[:ind+1]

    for i in range(ind, N):
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


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]

intervals = [[1, 5]]
newInterval = [0, 0]
newInterval = [6, 8]

intervals = [[1, 5]]
newInterval = [5, 7]


intervals = [[0, 3], [4, 6], [8, 10]]
newInterval = [7, 13]

intervals = [[0, 2], [3, 3], [6, 11]]
newInterval = [9, 15]
print(insert(intervals, newInterval))
