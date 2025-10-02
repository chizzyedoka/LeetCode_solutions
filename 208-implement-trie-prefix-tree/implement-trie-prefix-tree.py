class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = dict()
        self.is_last = False

class Trie:

    def __init__(self):
        self.trie = TrieNode('#')

    def insert(self, word: str) -> None:
        root = self.trie
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode(char)
            root = root.children[char]
        root.is_last = True

    def search(self, word: str) -> bool:
        root = self.trie
        for char in word:
            if char not in root.children:
                return False
            root = root.children[char]
        return root.is_last
        

    def startsWith(self, prefix: str) -> bool:
        root = self.trie
        for char in prefix:
            if char not in root.children:
                return False
            root = root.children[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)