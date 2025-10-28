class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        def isValid(string):
            count = 0
            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        # BFS setup
        queue = deque([s])
        visited = set([s])
        valid = []
        found = False

        while queue:
            cur = queue.popleft()

            if isValid(cur):
                valid.append(cur)
                found = True

            # once we find valid strings, we don't generate deeper ones
            if found:
                continue

            # generate all possible strings by removing one parenthesis
            for i in range(len(cur)):
                if cur[i] not in ('(', ')'):
                    continue
                newStr = cur[:i] + cur[i+1:]
                if newStr not in visited:
                    visited.add(newStr)
                    queue.append(newStr)

        return valid
