class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        order_dict = {}
        for i, char in enumerate(order):
            order_dict[char] = i

        def isVerified(word1, word2, index):
            while index < min(len(word1), len(word2)):
                char1, char2 = word1[index], word2[index]
                if char1 != char2:
                    if order_dict[char1] > order_dict[char2]:
                        return False
                    return True
                index += 1
            if word1 > word2:
                return False
            return True

        
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            if not isVerified(word1, word2, 0):
                return False
        return True