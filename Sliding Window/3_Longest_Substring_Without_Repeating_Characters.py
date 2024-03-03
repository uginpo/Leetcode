def lengthOfLongestSubstring(s: str) -> int:
    print(s)
    if len(s) == 0:
        return 0
    l, max_len = 0, 1
    r = 0
    N = len(s)

    while r < N-1:

        if s[r+1] in s[l:r+1]:
            l += 1
        else:
            r += 1

        max_len = max(max_len, r-l+1)

    return max_len


s = "bbbbb"
s = "abcabcbb"
s = "au"
s = "dvdf"
s = "aabaab!bb"
s = "pwwkew"
s = "bbtablud"
print(lengthOfLongestSubstring(s))
