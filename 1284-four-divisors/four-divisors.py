class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        cache = {}

        def getDivisors(num:int) -> List[int]:
            divisors = set()
            if num in cache:
                return cache[num]

            for i in range(1,int(sqrt(num)+1)):
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num//i)

            cache[num] = divisors


            return divisors 

        sum_of_four_divisors = 0
        for num in nums:
            divisors = getDivisors(num)
            if len(divisors) == 4:                
                sum_of_four_divisors += sum(divisors)

        return sum_of_four_divisors
