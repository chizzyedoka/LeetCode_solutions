class ListNode:
    def __init__(self, freq):
        self.freq = freq
        self.keys = set()
        self.next = None
        self.prev = None

class AllOne:

    def __init__(self):
        self.str_to_node = {}
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        # (1, [leet]) <-> (2, [hello]) <-> (3, [world, code])
        # {leet: (1, [leet]), hello: (2, [hello]), world: (3, [world, code]), code: (3, [world, code]) }

    def insertAfter(self, node, newNode):
        nextNode = node.next
        node.next = newNode
        newNode.prev = node
        newNode.next = nextNode
        nextNode.prev = newNode

    def inc(self, key: str) -> None:
        if key not in self.str_to_node:
            if self.head.next == self.tail or self.head.next.freq != 1:
                newNode = ListNode(1)
                newNode.keys.add(key)
                self.insertAfter(self.head, newNode)
            else:
                self.head.keys.add(key)
            self.str_to_node[key] = self.head.next
            return

        # try removing leet
        node = self.str_to_node[key]
        node.keys.remove(key)  # (1, []) <-> (2, [hello]) <-> (3, [world, code])
        freq = node.freq
        nextNode = node.next

        if nextNode == self.tail or nextNode.freq != freq + 1:  # determine where to put leet
            newNode = ListNode(freq+1)
            newNode.keys.add(key)
            self.insertAfter(node, newNode)
        else: 
            nextNode.keys.add(key)
            newNode = nextNode
        self.str_to_node[key] = newNode

        if not node.keys:
            self.remove(node)
        

    def dec(self, key: str) -> None:
        if key not in self.str_to_node:
            return
        node = self.str_to_node[key]
        node.keys.remove(key)
        freq = node.freq
        if freq > 1:
            freq -= 1
            # now move the key in linked list to previous node
            prevNode = node.prev
            if prevNode == self.head or prevNode.freq != freq: # node doesnt exist
                newNode = ListNode(freq)
                newNode.keys.add(key)
                newNode.next = node
                newNode.prev = prevNode
                prevNode.next = newNode
                node.prev = newNode
                self.str_to_node[key] = newNode
            else:
                prevNode.keys.add(key)
                self.str_to_node[key] = prevNode

            if not node.keys:
                self.remove(node)

        else: # freq becomes negative, so remove string from hashmap
            del str_to_node[key]

    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    def getMaxKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        
        return next(iter(self.head.next.keys))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

class ListNode:
    def __init__(self, freq):
        self.freq = freq
        self.keys = set()
        self.next = None
        self.prev = None

class AllOne:

    def __init__(self):
        self.str_to_node = {}
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertAfter(self, node, newNode):
        nextNode = node.next
        node.next = newNode
        newNode.prev = node
        newNode.next = nextNode
        nextNode.prev = newNode

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = node.prev = None

    def inc(self, key: str) -> None:
        if key not in self.str_to_node:
            if self.head.next == self.tail or self.head.next.freq != 1:
                newNode = ListNode(1)
                newNode.keys.add(key)
                self.insertAfter(self.head, newNode)
            else:
                self.head.next.keys.add(key)
            self.str_to_node[key] = self.head.next
            return

        node = self.str_to_node[key]
        node.keys.remove(key)
        freq = node.freq
        nextNode = node.next
        if nextNode == self.tail or nextNode.freq != freq + 1:
            newNode = ListNode(freq + 1)
            newNode.keys.add(key)
            self.insertAfter(node, newNode)
        else:
            nextNode.keys.add(key)
            newNode = nextNode
        self.str_to_node[key] = newNode

        if not node.keys:
            self.remove(node)

    def dec(self, key: str) -> None:
        if key not in self.str_to_node:
            return

        node = self.str_to_node[key]
        node.keys.remove(key)
        freq = node.freq

        if freq > 1:
            prevNode = node.prev
            if prevNode == self.head or prevNode.freq != freq - 1:
                newNode = ListNode(freq - 1)
                newNode.keys.add(key)
                self.insertAfter(prevNode, newNode)
            else:
                prevNode.keys.add(key)
                newNode = prevNode
            self.str_to_node[key] = newNode
        else:
            del self.str_to_node[key]

        if not node.keys:
            self.remove(node)

    def getMaxKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))
