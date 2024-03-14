def isHappy(n: int) -> bool:
    res = set()

    while True:
        if n == 1:
            return True
        else:
            s = list(str(n))
            n = sum((int(x))**2 for x in s if x != 0)
            if n in res:
                return False
            else:
                res.add(n)


n = 2
n = 0
n = 19
print(isHappy(n))
