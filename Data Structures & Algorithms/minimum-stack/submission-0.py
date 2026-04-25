class MinStack:

    def __init__(self):
        self.stack = [] # initialize an array, Python implementation of a regular stack
        self.minStack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int: # this function will only be called when stack is non-empty
        return self.minStack[-1]
