class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        import heapq
        arr = []
        heapq.heapify(nums)
        while nums:
            alice = heapq.heappop(nums)
            bob = heapq.heappop(nums)
            arr.append(bob)
            arr.append(alice)
        return arr
        