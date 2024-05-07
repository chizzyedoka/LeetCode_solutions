class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashMap = Counter(tasks)
        maxHeap = []
        q = deque()
        for char in hashMap:
            heapq.heappush(maxHeap,-hashMap[char])
        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                cnt += 1
                if cnt:
                    q.append((cnt,n+time))
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time