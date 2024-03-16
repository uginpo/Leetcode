from math import inf


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if self.stack:
            min_val = min(val, self.min_stack[-1])

        else:
            min_val = val

        self.stack.append(val)
        self.min_stack.append(min_val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int | None:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int | None:
        if self.stack:
            return self.min_stack[-1]
        return None
