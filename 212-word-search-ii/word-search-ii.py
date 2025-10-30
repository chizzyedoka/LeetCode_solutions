class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # create a prefix tree from words
        root = TrieNode()
        for word in words:
            current_node = root
            for char in word:
                if char not in current_node.children:
                    current_node.children[char] = TrieNode()
                current_node = current_node.children[char]
            current_node.isEndOfWord = True
            current_node.word = word

        rows, cols = len(board), len(board[0])

        def dfs(r, c, current_node):
            row_inbounds = 0 <= r < rows
            col_inbounds = 0 <= c < cols
            if not row_inbounds or not col_inbounds or (r,c) in visited or board[r][c] not in current_node.children:
                return 

            char = board[r][c]
            next_node = current_node.children[char]
            if next_node.isEndOfWord:
                result.add(next_node.word)
            visited.add((r,c))

            dfs(r+1, c, next_node)  
            dfs(r-1, c, next_node) 
            dfs(r, c+1, next_node) 
            dfs(r, c-1,  next_node)

            visited.remove((r,c))

        
        
        visited = set()
        result = set()
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return list(result)
                
