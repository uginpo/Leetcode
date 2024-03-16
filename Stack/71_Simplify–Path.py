def simplifyPath(path: str) -> str:
    stack = []
    current = ""

    for s in path + "/":
        if s == "/":
            if current == "..":
                if stack:
                    stack.pop()

            elif current != "" and current != ".":
                stack.append(current)

            current = ""

        else:
            current += s

    return "/" + "/".join(stack)


path = "/../"
path = "/home/"
print(simplifyPath(path))
