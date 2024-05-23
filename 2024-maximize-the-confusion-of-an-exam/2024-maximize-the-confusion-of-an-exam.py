class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        answer_map = {'T':0, 'F':0}
        window_start = 0
        res = 0
        for window_end in range(len(answerKey)):
            char = answerKey[window_end]
            answer_map[char] += 1
            max_freq = max(answer_map.values())
            while window_end-window_start+1 > k+max_freq:
                answer_map[answerKey[window_start]] -= 1
                window_start+=1 
            res = max(res, window_end-window_start+1)
        return res