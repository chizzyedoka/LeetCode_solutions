class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1 = rec1[0]
        y1 = rec1[1]
        x2 = rec1[2]
        y2 = rec1[3]

        x3 = rec2[0]
        y3 = rec2[1]
        x4 = rec2[2]
        y4 = rec2[3]

        if x2 <= x3 or x4 <= x1:
            return False
        
        if y2 <= y3 or y4 <= y1:
            return False
        return True
