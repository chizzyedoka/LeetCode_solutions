# brute force
class MapSum:

    def __init__(self):
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        _sum = 0
        for key in self.map.keys():
            if prefix in key[:len(prefix)]:
                _sum += self.map[key]
        return _sum        

class TrieNode:
    def __init__(self,char):
        self.char = char
        self.children = dict()
        self.score = 0 # store sum of values of all words passing this node

class MapSum:

    def __init__(self):
        self.map = {} # keep track of previous key->value to handle updates
        self.root = TrieNode("#")

    def insert(self, key: str, val: int) -> None:
        # delta = new value - old value (to handle updates properly)
        delta = val - self.map.get(key, 0)
        self.map[key] = val

        root = self.root
        for char in key:
            if char not in root.children:
                root.children[char] = TrieNode(char)
            root = root.children[char]
            root.score += delta   # update prefix sum along the path

       

    def sum(self, prefix: str) -> int:
        root = self.root
        for char in prefix:
            if char not in root.children:
                return 0
            root = root.children[char]
        return root.score
               

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)