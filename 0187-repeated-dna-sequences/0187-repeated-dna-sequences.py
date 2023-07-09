class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        k = 10
        seen = set()
        result = set()
        for i in range(len(s)-k+1):
            sequence = s[i:i+k]
            if sequence in seen:
                result.add(sequence)
            seen.add(sequence)
        return result
                
        