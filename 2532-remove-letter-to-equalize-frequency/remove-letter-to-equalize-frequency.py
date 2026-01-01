class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = defaultdict(int) #  {b:0,a:1.c:1}

        for char in word:
            counter[char] += 1

        for char in word:

            counter[char] -= 1

            if counter[char] == 0:
                del counter[char]
                
            if len(set(counter.values())) == 1:
                return True

            counter[char] += 1

        return False