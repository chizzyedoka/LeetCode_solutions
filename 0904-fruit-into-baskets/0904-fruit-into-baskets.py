
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hashmap = {}
        window_start = 0
        max_fruits = 0
        for window_end in range(len(fruits)):
            fruit = fruits[window_end]
            if fruit not in hashmap:
                hashmap[fruit] = 0
            hashmap[fruit] += 1
            while len(hashmap) > 2:
                hashmap[fruits[window_start]] -= 1
                if hashmap[fruits[window_start]] == 0:
                    del hashmap[fruits[window_start]]
                window_start += 1
            max_fruits = max(max_fruits, window_end-window_start+1)
        return max_fruits
