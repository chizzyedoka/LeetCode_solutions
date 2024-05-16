class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        longest_same, window_start = 0,0
        for window_end in range(len(s)):
            char = s[window_end]
            if char not in hashmap:
                hashmap[char] = 0
            hashmap[char] += 1
            #longest_same = max(longest_same, hashmap[char])
            while (window_end - window_start + 1 - max(hashmap.values())) > k:
                left_char = s[window_start]
                hashmap[left_char] -= 1
                window_start += 1
            longest_same = max(longest_same, window_end-window_start+1)
        return longest_same
                