class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            count_tuple = tuple(count)
            if count_tuple not in map:
                map[count_tuple] = []
            map[count_tuple].append(word)
        return map.values()

    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     map = {}
    #     for word in strs:
    #         if tuple(sorted(word)) not in map:
    #             map[tuple(sorted(word))] = []
    #         map[tuple(sorted(word))].append(word)
    #     return map.values()
            
            



        

        