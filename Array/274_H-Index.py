def hIndex(citations: list[int]) -> int:
    citations = sorted(citations, reverse=True)
    print(citations)
    for ind, val in enumerate(citations):
        if ind >= val:
            return ind
    return (len(citations))


citations = [2, 0, 6, 1, 5]
citations = [3, 0, 6, 1, 5]
print(hIndex(citations))
