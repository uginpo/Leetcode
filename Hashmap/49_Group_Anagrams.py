from collections import defaultdict


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams_dict = defaultdict(list)

    for word in strs:
        anagrams_dict[tuple(sorted(word))].append(word)

    return list(anagrams_dict.values())


strs = [""]
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(groupAnagrams(strs))
