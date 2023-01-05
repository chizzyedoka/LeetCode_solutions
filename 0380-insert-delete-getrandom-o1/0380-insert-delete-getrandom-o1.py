class RandomizedSet:

    def __init__(self):
        self.numList = []
        self.numMap = {}
        self.index = 0
        

    def insert(self, val: int) -> bool:
        if val in self.numMap:
            return False
        self.numMap[val] = len(self.numList)
        self.numList.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numMap:
            return False
        index = self.numMap[val]
        last_element = self.numList[-1]
        self.numMap[last_element] = index
        self.numList[index] = last_element
        self.numList.pop()
        del self.numMap[val]
        return True
    

    def getRandom(self) -> int:
        return random.choice(self.numList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()