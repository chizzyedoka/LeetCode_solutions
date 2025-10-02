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


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)