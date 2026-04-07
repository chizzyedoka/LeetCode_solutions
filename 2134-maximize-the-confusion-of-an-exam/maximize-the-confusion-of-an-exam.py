class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # max count(T, F) in that window
        # slide window when k has been exhausted
        bool_map = {'F':0, 'T':0}
        start = 0
        result = 0

        for end in range(len(answerKey)):
            bool_map[answerKey[end]] += 1

            window = end - start + 1
            while (window - max(bool_map.values()) > k ):
                bool_map[answerKey[start]] -= 1
                start += 1
                window = end - start + 1

            result = max(result, window)

        return result    