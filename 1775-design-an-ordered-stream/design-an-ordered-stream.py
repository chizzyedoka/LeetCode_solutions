class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.pointer = 0
        self.data = [None] * (n+1)

    def insert(self, idKey: int, value: str) -> List[str]:
        self.data[idKey-1] = value
        result = []
        while self.pointer < self.n and self.data[self.pointer]:
            result.append(self.data[self.pointer])
            self.pointer += 1
        return result



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)