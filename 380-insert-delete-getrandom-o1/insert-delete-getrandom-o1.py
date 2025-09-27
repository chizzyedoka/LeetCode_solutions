class RandomizedSet:

    def __init__(self):
        self.itemsList = []
        self.itemsDict = {}

    def insert(self, val: int) -> bool:
        if val not in self.itemsDict:
            self.itemsList.append(val)
            self.itemsDict[val] = len(self.itemsList) - 1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val not in self.itemsDict:
            return False
        lastElement = self.itemsList[-1]
        indexToRemove = self.itemsDict[val]
        # swap lastElement and value we want to remove
        self.itemsList[indexToRemove], self.itemsList[-1] = lastElement, self.itemsList[indexToRemove]
        self.itemsDict[lastElement] = indexToRemove
        self.itemsList.pop()
        del self.itemsDict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.itemsList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()