class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s, t):
            if len(s) != len(t):
                return False
            return sorted(s) == sorted(t)

        res = []
        seen = set()

        for i in range(len(strs)):
            if i in seen:
                continue
            word1 = strs[i]
            anagramsOfWord = [word1]
            for j in range(i+1, len(strs)):
                word2 = strs[j]
                if isAnagram(word1, word2) and j not in seen:
                    anagramsOfWord.append(word2)
                    seen.add(j)
            res.append(anagramsOfWord)
        return res
    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            # Sort the word and use it as the key
            sorted_word = tuple(sorted(word))
            anagrams[sorted_word].append(word)

        print(anagrams)
        # Return the groups of anagrams
        return list(anagrams.values())



            
            



        

        