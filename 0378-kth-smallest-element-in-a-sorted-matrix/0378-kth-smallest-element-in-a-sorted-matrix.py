class Solution:
    def kthSmallest(self,matrix, k):
        def count_less_equal(x):
            count, j = 0, len(matrix[0]) - 1
            for i in range(len(matrix)):
                while j >= 0 and matrix[i][j] > x:
                    j -= 1
                count += (j + 1)
            return count

        n = len(matrix)
        low, high = matrix[0][0], matrix[n - 1][n - 1]

        while low < high:
            mid = (low + high) // 2
            if count_less_equal(mid) < k:
                low = mid + 1
            else:
                high = mid

        return low

# class Solution:
#     def kthSmallest(self, matrix, k):
#         rows = len(matrix)
#         cols = len(matrix[0])

#         lo = matrix[0][0]
#         hi = matrix[rows - 1][cols - 1]

#         while lo <= hi:
#             mid = lo + (hi - lo) // 2
#             count = 0
#             max_num = lo

#             for r in range(rows):
#                 c = cols - 1
#                 while c >= 0 and matrix[r][c] > mid:
#                     c -= 1

#                 if c >= 0:
#                     count += (c + 1)
#                     max_num = max(max_num, matrix[r][c])
#                 else:
#                     break

#             if count == k:
#                 return max_num
#             elif count < k:
#                 lo = mid + 1
#             else:
#                 hi = mid - 1

#         return lo
# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         minHeap = []
#         n = len(matrix)
#         row,col = 0,0
        
#         for row in range(n):
#             node = matrix[row][col], (row,col)
#             heapq.heappush(minHeap, node)
#         print(minHeap)
        
#         myList = []
#         for i in range(k):
#             val,(row,col) = heapq.heappop(minHeap)
#             myList.append(val)
#             if col < n-1:
#                 new_node = matrix[row][col+1], (row,col+1)
#                 heapq.heappush(minHeap, new_node)
#         print(myList)
#         return val
            
                
            
            
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
#         n = len(matrix) # 3
#         row, col = 0,0
#         minHeap = []
        
#         while row < n: # 0, 1, 2
#             node = (matrix[row][col], (row,col)) # val, position
#             heapq.heappush(minHeap, node)
#             row += 1
            
#         for i in range(k):
#             val, coord = heapq.heappop(minHeap)
#             row,col = coord
#             if col < n-1:
#                 new_node = (matrix[row][col+1], (row,col+1))
#                 heapq.heappush(minHeap, new_node)
#         return val
                
                
        