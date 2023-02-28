class MinStack:

    def __init__(self):
        self.myStack = []

    def push(self, val: int) -> None:
        self.myStack.append(val)

    def pop(self) -> None:
        self.myStack.pop()

    def top(self) -> int:
        return self.myStack[-1]

    def getMin(self) -> int:
        return min(self.myStack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()