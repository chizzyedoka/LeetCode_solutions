class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        seen = deque()
        for end in range(len(s)):
            seen.append(s[end])
            if len(seen) == 3:
                print(seen)
                if len(set(seen)) == 3:
                    count += 1
                seen.popleft()
        #print(count)
        return count
    


        