class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n, m = len(g)-1, len(s)-1
        count = 0
        while n >= 0 and m >= 0:
            if s[m] >= g[n]:
                count += 1
                n -= 1
                m -= 1
            else:
                n -=1
        return count

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         g.sort()
#         s.sort()

#         a = len(g) - 1
#         b = len(s) - 1
#         maxs = 0

#         while a >= 0 and b >= 0:
#             if s[b] >= g[a]:
#                 maxs += 1
#                 a -= 1
#                 b -= 1
#             else:
#                 a -= 1
#         return maxs
# class Solution:
#     def findContentChildren(self, g: List[int], s: List[int]) -> int:
#         count = 0
#         if len(s) >= len(g):
#             for i in range(len(g)):
#                 if s[i] >= g[i]:
#                     count += 1
#         else:
#             for i in range(len(s)):
#                 if g[i] <= s[i]:
#                     count += 1
#         return count
        