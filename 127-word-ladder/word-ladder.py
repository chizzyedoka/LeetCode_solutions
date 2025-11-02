class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if beginWord == endWord or not wordList or endWord not in wordList:
            return 0

        # build graph
        graph = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                transformed_word = word[:i] + "*" + word[i+1:]
                graph[transformed_word].append(word)

        # find distance

        visited = set()
        queue = deque()
        queue.append((beginWord, 1))
        

        while queue:
            current_word, distance = queue.popleft()
            if current_word == endWord:
                return distance
            
            visited.add(current_word)

            for i in range(len(current_word)):
                transformed_word = current_word[:i] + "*" + current_word[i+1:]

                potential_words = graph.get(transformed_word, None)

                if not potential_words:
                    continue
                for potential_word in potential_words:
                    if potential_word not in visited:
                        visited.add(potential_word)
                        queue.append((potential_word, distance+1))

        return 0