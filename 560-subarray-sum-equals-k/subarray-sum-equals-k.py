class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        cur_sum = 0
        prefix_dict = defaultdict(int)
        prefix_dict[0] = 1

        for num in nums:
            cur_sum += num
            
            if cur_sum -k in prefix_dict:
                result += prefix_dict[cur_sum-k]

            prefix_dict[cur_sum] += 1

        return result