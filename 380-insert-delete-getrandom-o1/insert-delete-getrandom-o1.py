class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.dict[val] = len(self.arr)
            self.arr.append(val)
            return True
        return False
            
    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False

        # get values position
        val_pos = self.dict[val]
        last_val = self.arr[-1]
        
        # swap val_pos with last ele in arr
        self.arr[val_pos], self.arr[-1] = self.arr[-1], self.arr[val_pos]

        # update new positions in dict
        self.dict[val] = len(self.arr) - 1
        self.dict[last_val] = val_pos

        # remove from arr and dict
        self.arr.pop()
        del self.dict[val]
        return True


    def getRandom(self) -> int:
        return random.choice(self.arr)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# we use a dict to insert in o(1)
# we can also remove from a dict in o(1)
# for random it has to be an array
# problem is, when a value as been removed from a dict, how do we replicate that in the arr
# we have to move that value to the end of the arr so removing it is in O(1)

# {2: 0, 5: 1, 3:2, 6:3}
# [2, 5, 3, 6]

# to remove 5 from the list, we need to
# 1. swap 5's position with the last element [2, 6, 3, 5]
# 2. update the position in the dict. why? so subsequent values are in their correct pos
# {2: 0, 5:3, 3:2, 6:1}
# 3. delete it from the dict and pop from the arr


# how do we combine these two data structures