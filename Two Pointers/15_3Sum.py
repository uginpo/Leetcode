from itertools import permutations


def threeSum(nums: list[int]) -> list[tuple[int]]:

    triples = set()
    neg = [x for x in nums if x < 0]
    pos = [x for x in nums if x > 0]
    zer = [x for x in nums if x == 0]

    p = set(pos)
    n = set(neg)
    N = len(neg) - 1
    P = len(pos) - 1

    if zer:
        for num in n:
            if abs(num) in p:
                triples.add((num, 0, -num))
    if len(zer) >= 3:
        triples.add((0, 0, 0))

    for x1, x2 in permutations(neg, 2):
        couple = x1 + x2
        if -couple in p:
            lst = tuple(sorted((x1, x2, -couple)))
            triples.add(lst)

    for x1, x2 in permutations(pos, 2):
        couple = x1 + x2
        if -couple in n:
            lst = tuple(sorted((x1, x2, -couple)))
            triples.add(lst)

    return list(triples)


nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1,-1,2],[-1,0,1]]
nums = [0, 0, 0]
nums = [1, 1, -2]
nums = [1, 1, 1]
nums = [-1, 0, 1, 0]
nums = [1, 2, -2, -1]
nums = [0, 1, 1]
nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
# [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
nums = [-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0]
# [[-5,1,4],[-4,0,4],[-4,1,3],[-2,-2,4],[-2,1,1],[0,0,0]]
print(threeSum(nums))
