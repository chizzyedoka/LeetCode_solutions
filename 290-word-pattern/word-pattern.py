class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        
        charToWord = {}
        wordToChar = {}
        for i in range(len(pattern)):
            char = pattern[i]
            word = s[i]
            if char in charToWord and charToWord[char] != word:
                return False
            if word in wordToChar and wordToChar[word] != char:
                return False
            charToWord[char] = word
            wordToChar[word] = char
        return True