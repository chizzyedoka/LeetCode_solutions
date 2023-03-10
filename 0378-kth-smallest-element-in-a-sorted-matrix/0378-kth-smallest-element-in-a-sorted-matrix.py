class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix) # 3
        row, col = 0,0
        minHeap = []
        
        while row < n: # 0, 1, 2
            node = (matrix[row][col], (row,col)) # val, position
            heapq.heappush(minHeap, node)
            row += 1
            
        for i in range(k):
            val, coord = heapq.heappop(minHeap)
            row,col = coord
            if col < n-1:
                new_node = (matrix[row][col+1], (row,col+1))
                heapq.heappush(minHeap, new_node)
        return val
                
                
        