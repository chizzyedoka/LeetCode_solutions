class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # ABAA K = 1
        # GET ur window
        # slide the window when u have k different letters
        # "AABABBA", k = 1
        # {A:2, B:1}
        result = 0
        start = 0
        max_count = 0
        char_count = defaultdict(int)
        for end in range(len(s)):
            char = s[end]
            char_count[char] += 1
            window = end - start + 1
            max_count = max(max_count, char_count[char])
            # shrink window while window is invalid
            while window - max_count > k: 
                left_char = s[start]
                char_count[left_char] -= 1
                start += 1
                window = end - start + 1

            result = max(result, window)

        return result