def isSubsequence(s: str, t: str) -> bool:
    ind = 0
    for symb in s:
        ind_s = t.find(symb, ind)
    if ind_s == -1:
        return False
    else:
        ind = ind_s+1

    return True


s = "abc"
t = "ahbgdc"

print(isSubsequence(s, t))
