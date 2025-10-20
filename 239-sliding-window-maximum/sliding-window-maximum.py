class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = deque()
        n = len(nums)

        for i in range(k):
            num = nums[i]
            while q and nums[q[-1]] <= num:
                q.pop()
            q.append(i)
        result.append(nums[q[0]])

        for i in range(k, n):
            if q and i - q[0] == k:
                q.popleft()

            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            result.append(nums[q[0]])
        return result
            
