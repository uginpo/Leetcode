def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)


haystack = "sadbutsad"
needle = "sad"
haystack = "leetcode"
needle = "leeto"
print(strStr(haystack, needle))
