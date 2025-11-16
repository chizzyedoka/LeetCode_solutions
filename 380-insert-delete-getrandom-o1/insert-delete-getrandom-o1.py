class RandomizedSet:

    def __init__(self):
        self.items = [] # [100, 300, 500]
        self.dict = {} # {100: 0, 300:1, 500:2}
        

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        
        self.dict[val] = len(self.items)
        self.items.append(val)
        return True
        

    def remove(self, val: int) -> bool: # remove 300
        if val not in self.dict:
            return False
        indexToRemove = self.dict[val]
        lastElement = self.items[-1]
        # swap val with last val
        self.items[indexToRemove], self.items[-1] = self.items[-1], self.items[indexToRemove] # [100, 500, 300]
        self.dict[lastElement] = indexToRemove     # {100: 0, 500:1, 300:2}
        self.items.pop()
        del self.dict[val] # {100: 0, 500:1, 
        return True

        

    def getRandom(self) -> int:
        return random.choice(self.items)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()