def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


s = "anagram"
t = "nagaram"

s = "aacc"
t = "ccaa"
print(isAnagram(s, t))
