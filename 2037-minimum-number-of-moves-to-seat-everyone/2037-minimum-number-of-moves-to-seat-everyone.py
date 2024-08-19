class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        res = 0
        n = len(seats)
        for i in range(n):
            res += abs(seats[i] - students[i])
        return res