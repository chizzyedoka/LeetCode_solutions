class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        left = [-1] * n
        right = [n] * n
        
        # Fill left array with distances to the nearest occupied seat on the left
        for i in range(n):
            if seats[i] == 1:
                left[i] = i
            elif i > 0:
                left[i] = left[i-1]
        
        # Fill right array with distances to the nearest occupied seat on the right
        for i in range(n-1, -1, -1):
            if seats[i] == 1:
                right[i] = i
            elif i < n-1:
                right[i] = right[i+1]
        
        # Calculate the maximum distance to the closest occupied seat
        max_dist = 0
        for i in range(n):
            if seats[i] == 0:
                left_dist = float('inf') if left[i] == -1 else i - left[i]
                right_dist = float('inf') if right[i] == n else right[i] - i
                max_dist = max(max_dist, min(left_dist, right_dist))
        
        return max_dist