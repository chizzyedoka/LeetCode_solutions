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

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagrams = defaultdict(list)
        for word in strs:
            bucket = [0] * 26
            for letter in word:
                bucket[ord(letter) - ord('a')] += 1
            tuple_bucket = tuple(bucket)
            anagrams[tuple_bucket].append(word)

        for word, word_anagram in anagrams.items():
            result.append(word_anagram)
        return result