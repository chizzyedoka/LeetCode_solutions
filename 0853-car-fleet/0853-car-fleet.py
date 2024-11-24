class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
            
        cars = sorted(zip(position, speed), key=lambda x: -x[0])
        stack = []
        for pos, spd in cars:
            time_to_target = (target - pos) / spd
            if not stack or time_to_target > stack[-1]:
                stack.append(time_to_target)
        return len(stack)
            