def mergeTwoLists(list1, list2) -> list:
    if not list1:
        return list2

    if not list2:
        return list1

    result = []
    i = j = 0
    N = len(list1)
    M = len(list2)

    while True:
        a = list1[i]
        b = list2[j]
        if a == b:
            result.extend([a, b])
            i += 1
            j += 1
        elif a < b:
            result.append(a)
            i += 1
        else:
            result.append(b)
            j += 1

        if i == N and j < M:
            result.extend(list2[j:])
            break
        elif i < N and j == M:
            result.extend(list1[i:])
            break
        elif i == N and j == M:
            break

    return result


list1 = [1, 2, 4]
list2 = [1, 3, 4]

list1 = []
list2 = [0]

print(mergeTwoLists(list1, list2))
