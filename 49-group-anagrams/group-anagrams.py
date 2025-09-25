class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        result = []
        for word in strs:
            sorted_word = "".join(sorted(word))
            anagrams[sorted_word].append(word)

        for word, word_anagram in anagrams.items():
            result.append(word_anagram)
        return result