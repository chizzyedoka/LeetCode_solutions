# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left= 1
        right = n
        ans = -1
        while left <= right:
            mid = (left+right)//2
            # fist half isn't a bad version
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid - 1
                ans = mid
        return ans
        