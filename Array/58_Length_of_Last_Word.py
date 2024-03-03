def lengthOfLastWord(s: str) -> int:
    a = len(s.strip().split()[-1])
    return a


s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))
