class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):

            # already processed
            if nums[i] == 0:
                continue

            slow = i
            fast = i

            # direction we must maintain
            direction = nums[i] > 0

            while True:

                # move slow once
                next_slow = next_index(slow)

                # direction changed
                if (nums[next_slow] > 0) != direction:
                    break

                # self loop
                if next_slow == slow:
                    break

                slow = next_slow

                # move fast first step
                next_fast = next_index(fast)

                if (nums[next_fast] > 0) != direction:
                    break

                if next_fast == fast:
                    break

                # move fast second step
                next_fast2 = next_index(next_fast)

                if (nums[next_fast2] > 0) != direction:
                    break

                if next_fast2 == next_fast:
                    break

                fast = next_fast2

                if slow == fast:
                    return True

            # mark path as visited
            current = i

            while nums[current] != 0 and (nums[current] > 0) == direction:
                nxt = next_index(current)
                nums[current] = 0
                current = nxt

        return False