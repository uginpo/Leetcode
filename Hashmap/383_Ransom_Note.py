from collections import defaultdict


def canConstruct(ransomNote: str, magazine: str) -> bool:
    mag_dict = defaultdict(int)
    for letter in magazine:
        mag_dict[letter] += 1

    for letter in ransomNote:
        mag_dict[letter] -= 1
        if mag_dict[letter] < 0:
            return False
    return True


ransomNote = "a"
magazine = "ba"
print(canConstruct(ransomNote, magazine))
