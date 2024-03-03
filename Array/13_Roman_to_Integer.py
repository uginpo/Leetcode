def romanToInt(s: str) -> int:

    romans = {
        "V": 5,
        "X": 10,
        "I": 1,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    number = 0
    n = len(s)
    for i in range(n):
        num = romans[s[i]]
        if i < n-1:
            if num < romans[s[i+1]]:
                num = - num
        number += num

    return number


# CM = 900, XC = 90 and IV = 4
s = "LVIII"
s = "MCDLXXVI"
s = "MCMXCIV"
print(romanToInt(s))
