from collections import defaultdict


def isIsomorphic(s: str, t: str) -> bool:
    if len(set(s)) != len(set(t)):
        return False
    t_dict = {x: set() for x in s}

    for symb_s, symb_t in zip(s, t):
        a = t_dict[symb_s]
        a.add(symb_t)
        if len(a) > 1:
            return False

    return True


s = "bbbaaaba"
t = "aaabbbba"
s = "egg"
t = "add"

print(isIsomorphic(s, t))
