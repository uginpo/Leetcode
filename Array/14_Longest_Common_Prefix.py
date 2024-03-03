def longestCommonPrefix(strs: list[str]) -> str:
    N = min(map(len, strs))
    etalon = strs[0]
    # N = len(etalon)
    n = len(strs)
    pref = []
    flag = True
    for i in range(N):
        for j in range(1, n):
            if etalon[i] != strs[j][i]:
                flag = False
                break
        if flag == False:
            return ''.join(pref)
        else:
            pref.append(etalon[i])
    return ''.join(pref)


strs = ["dog", "racecar", "car"]
strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))
