def isValid(s: str) -> bool:
    open = {"(": ")",
            "[": "]",
            "{": "}"}

    close = {")": "(",
             "]": "[",
             "}": "{"}

    if len(s) == 0:
        return True

    stack = []
    N = len(s)

    for i in range(N):
        if len(stack) == 0:
            if s[i] in close:
                return False
            else:
                stack.append(s[i])

        elif stack[-1] in open:
            if s[i] in open:
                stack.append(s[i])
            else:
                if stack[-1] == close[s[i]]:
                    stack.pop()
                else:
                    return False

    return True if len(stack) == 0 else False


s = "()[]{}"
s = "(]"
print(isValid(s))
