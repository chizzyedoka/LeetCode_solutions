class ListNode:
    def __init__(self, key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key to Node
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node):   # head <-> 1 < -> 2 <-> 3 <-> 4 <-> tail
        # add node 5
        last_node = self.tail.prev # 4 <-> tail
        self.tail.prev = node # 5 <- tail  # 4 -> tail
        node.next = self.tail # 5 <-> tail
        last_node.next = node # 4 -> 5 <-> tail
        node.prev = last_node # 4 <-> 5 <-> tail



    def _remove(self, node): # 1 < -> 2 <-> 3 <-> 4
        nxt_node = node.next # 3 <-> 4
        prev_node = node.prev # 1
        node.prev.next = nxt_node # 1 -> 3 <-> 4
        nxt_node.prev = prev_node # 1 <-> 3 <-> 4

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # remove it from its position 
            self._remove(node)
            # add to the back, recently being used
            self._add(node)
            return node.val
        else:
            return -1

        

    def put(self, key: int, value: int) -> None:
        
        # check if we are updating a key
        if key in self.cache:
            old_node = self.cache[key]
            self._remove(old_node)
            old_node.val = value # edit its value, so we dont have to delete it from dictionary
            self._add(old_node)
            return

        # evict lru node if we've reached capacity
        if len(self.cache) == self.capacity:
            lru_node = self.head.next
            self._remove(lru_node)
            del self.cache[lru_node.key]
            self.head.next = lru_node.next
        
        # add new node
        node = ListNode(key, value)
        self._add(node)
        self.cache[key] = node
        return
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)