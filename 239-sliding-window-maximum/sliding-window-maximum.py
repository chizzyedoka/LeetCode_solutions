class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use a deque to keep the window valid -> max of k
        # minDeque -> front of the queue is the smallest ->monotonic increasing
        # maxDeque -> front of the deque is the maximum -> monotonic decreasing -> use this [7, 5, 3 ] 6

        queue = deque()
        n = len(nums)
        result = []

        for i in range(k):
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
        result.append(nums[queue[0]])

        for i in range(k, n):
            if queue and i - queue[0] >= k:
                queue.popleft()
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            result.append(nums[queue[0]])
        
        return result