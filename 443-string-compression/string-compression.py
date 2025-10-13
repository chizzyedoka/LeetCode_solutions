class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return chars
        group_count = 1
        index = 0
        n = len(chars)
        for i in range(1, n + 1):
            if i < n and chars[i] == chars[i - 1]:
                group_count += 1
            else:
                chars[index] = chars[i-1]
                index += 1
                if group_count > 1:
                    for digit in str(group_count):
                        chars[index] = digit
                        index += 1
                group_count = 1
       
        return index


