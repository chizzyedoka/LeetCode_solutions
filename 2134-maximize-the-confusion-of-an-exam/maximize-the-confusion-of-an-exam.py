class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # max count(T, F) in that window
        # slide window when k has been exhausted
        bool_map = {0:0, 1:0}
        start = 0
        result = 0

        for end in range(len(answerKey)):
            if answerKey[end] == "T":
                bool_map[1] += 1
            else:
                bool_map[0] += 1

            #window = end - start + 1
            while (end - start + 1 - max(bool_map.values()) > k ):
                if answerKey[start] == "T":
                    bool_map[1] -= 1
                else:
                    bool_map[0] -= 1
                start += 1

            result = max(result, end - start + 1)

        return result    