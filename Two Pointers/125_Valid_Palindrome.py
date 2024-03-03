def isPalindrome(s: str) -> bool:
    new_s = ''.join([symb.lower() for symb in s if symb.isalnum()])
    if len(new_s) <= 1:
        return True
    N = len(new_s)
    i = 0
    j = -1
    for i in range(N//2+1):
        print(new_s[i], new_s[j])
        if new_s[i] != new_s[j]:
            return False
        j -= 1

    return True


s = " "
s = "Abcfba"
s = "0z;z   ; 0"
print(isPalindrome(s))
