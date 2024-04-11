class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        s1,e1 =points[0]
        count = len(points)
        for i in range(1, len(points)):
            s2, e2 = points[i]
            if s2 <= e1:
                count -= 1
                s1, e1 = max(s1,s2), min(e1,e2)
            else:
                s1, e1 = s2, e2
        return count
            
        
#         if len(points) == 0:
#             return 0
#         points.sort()
#         arrow = 1
#         end = points[0][1]
#         for i in range(len(points)):
#             if points[i][0] > end:
#                 arrow += 1
#                 end = points[i][1]
#             else:
#                 end = min(end,points[i][1])
#         return arrow
            
        