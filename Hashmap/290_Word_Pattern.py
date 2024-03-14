
def wordPattern(pattern: str, s: str) -> bool:
    s_lst = s.split()

    if len(pattern) != len(s_lst):
        return False

    if len(set(pattern)) != len(set(s_lst)):
        return False

    t_dict = {x: set() for x in pattern}
    print(s_lst)
    for symb_s, symb_t in zip(pattern, s_lst):
        a = t_dict[symb_s]
        a.add(symb_t)
        if len(a) > 1:
            return False

    return True


pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s))
