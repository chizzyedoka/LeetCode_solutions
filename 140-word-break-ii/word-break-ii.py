class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}
        results = []

        def backtrack(s, word_set, current_sentence, results, start_index):
            if start_index == len(s):
                results.append(" ".join(current_sentence))
                return

            # Iterate over possible end indices
            for end_index in range(start_index+1, len(s)+1):
                word = s[start_index: end_index]
                if word in word_set:
                    current_sentence.append(word)
                    backtrack(s, word_set, current_sentence, results, end_index)
                    current_sentence.pop()

        backtrack(s, word_set, [], results, 0)
        return results
