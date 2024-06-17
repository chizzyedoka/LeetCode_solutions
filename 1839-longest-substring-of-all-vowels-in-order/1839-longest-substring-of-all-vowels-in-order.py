class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        window_start, res = 0, 0
        hashmap = {}
        queue = deque()
        for window_end in range(len(word)):
            char = word[window_end]
            if char not in hashmap:
                hashmap[char] = 0
            hashmap[char] += 1
            while queue and queue[-1] > char:# and window_start < window_end:
                removed = queue.popleft()
                hashmap[removed] -= 1
                if hashmap[removed] == 0:
                    del hashmap[removed]
                window_start += 1
            queue.append(char)
            if len(hashmap) == 5:
                res = max(res,window_end - window_start + 1)       
        return res



