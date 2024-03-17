def calculate(s: str) -> int | None:
    stack = []
    sign = 1
    res = 0
    curr = 0

    for elem in s:
        if elem.isdigit():
            curr = curr*10 + int(elem)

        elif elem in '+-':
            res += curr * sign
            curr = 0
            sign = -1 if elem == '-' else 1

        elif elem == '(':
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1

        elif elem == ')':
            res += curr * sign
            res *= stack.pop()
            res += stack.pop()
            curr = 0

    return res + curr * sign


s = "(1+(4+5+2)-3)+(6+8)"
print(calculate(s))
