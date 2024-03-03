def minWindow(s: str, t: str) -> str:
    if not s or not t:
        return ''

    Len_s = len(s)
    t_dict = {x: t.count(x) for x in t}
    s_dict = {}
    val_t_dict = len(t_dict)
    val_s_dict = 0

    l = 0
    res, resLen = [-1, -1], float('infinity')

    for r in range(Len_s):
        c = s[r]
        s_dict[c] = 1 + s_dict.get(c, 0)

        if c in t_dict and s_dict[c] == t_dict[c]:
            val_s_dict += 1

        while val_s_dict == val_t_dict:
            # update our result
            if (r - l + 1) < resLen:
                res = [l, r]
                resLen = (r - l + 1)
            # pop from the left of our window
            s_dict[s[l]] -= 1
            if s[l] in t_dict and s_dict[s[l]] < t_dict[s[l]]:
                val_s_dict -= 1
            l += 1

    l, r = res
    return s[l:r+1] if resLen != float("infinity") else ''

    print(f'{mn_window=}')
    return mn_window


s = "ADOBEODEBANC"
s = "ADOBECODEBANC"
t = "ABC"
s = "AA"
t = "AA"
# BANC

print(minWindow(s, t))
