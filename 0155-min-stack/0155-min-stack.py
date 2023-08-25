class MinStack:

    def __init__(self):
        self.myStack = []

    def push(self, val: int) -> None:
        # always push the minium element first in the stack
        if len(self.myStack) == 0:
            minVal = val
            print(val,minVal)
            self.myStack.append((val,minVal))
        else:
            minVal = self.myStack[-1][1]
            print(minVal)
            if val < minVal:
                minVal = val
            self.myStack.append((val,minVal))
            print(val,minVal)

    def pop(self) -> None:
        self.myStack.pop()

    def top(self) -> int:
        return self.myStack[-1][0]

    def getMin(self) -> int:
        return self.myStack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()