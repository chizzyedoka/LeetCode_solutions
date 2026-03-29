class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # [1,2,3,2,2,1]
        fruit_count = defaultdict(int)
        start = 0
        max_fruits = float("-inf")
        basket = set()

        for end in range(len(fruits)):
            fruit = fruits[end]
            fruit_count[fruit] += 1

            while len(fruit_count) > 2:
                fruit_count[fruits[start]] -= 1

                if fruit_count[fruits[start]] == 0:
                    del fruit_count[fruits[start]]

                start += 1

            window_size = end - start + 1
            max_fruits = max(max_fruits, window_size)

        return max_fruits



