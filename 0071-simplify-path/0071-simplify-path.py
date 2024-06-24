class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        res = ""
        
        i = 0
        while i < len(path):
            if path[i] == '/':
                i += 1
                continue
            
            temp = ""
            # Iterate till we traverse the whole string and encounter the next '/'
            while i < len(path) and path[i] != '/':
                temp += path[i]
                i += 1
            
            if temp == ".":
                continue
            elif temp == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(temp)
        
        # Adding all the stack elements to result
        while stack:
            res = "/" + stack.pop() + res
        
        # If no directory or file is present
        if not res:
            return "/"
        
        return res


