def evalRPN(tokens: list[str]) -> int | None:
    if len(tokens) == 1 and tokens[0].isdigit():
        return int(tokens[0])

    stack = []
    for elem in tokens:

        if elem not in '+-*/':
            stack.append(elem)
        else:
            second = int(stack.pop())
            first = int(stack.pop())

            match elem:
                case '+':
                    res = first + second

                case '-':
                    res = first - second

                case '*':
                    res = first * second

                case '/':
                    res = int(first / second)

            stack.append(str(res))

    return int(stack.pop())


tokens = ["2", "1", "+", "3", "*"]
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(evalRPN(tokens))
"""
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
    """
