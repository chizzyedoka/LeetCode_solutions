class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxes = sorted(boxTypes, key = lambda x: x[1], reverse=True)
        maxUnit = 0
        for box in boxes:
            if truckSize > box[0]:
                maxUnit += box[0] * box[1]
                truckSize -= box[0]
            else:
                maxUnit += truckSize * box[1]
                break
        return maxUnit