class Solution:
    def compress(self, chars: List[str]) -> int:
        s = []
        if not chars:
            return []
        group_count = 1
        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                group_count += 1
            else:
                s.append(chars[i - 1])
                if group_count > 1:
                    for digit in str(group_count):
                        s.append(digit)
                group_count = 1
        s.append(chars[-1])
        if group_count > 1:
            for digit in str(group_count):
                s.append(digit)
        chars[:] = s
        print(chars)
        return len(s)
