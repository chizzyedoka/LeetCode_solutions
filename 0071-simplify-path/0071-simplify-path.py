class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split the path by '/' to handle each component
        components = path.split('/')
        stack = []

        for component in components:
            if component == '' or component == '.':
                # Ignore empty components and current directory references
                continue
            elif component == '..':
                # Pop from the stack if there is a previous directory
                if stack:
                    stack.pop()
            else:
                # Push the directory name onto the stack
                stack.append(component)

        # Join the stack elements with '/' to form the simplified path
        return '/' + '/'.join(stack)

# Example usage:
solution = Solution()
path = "/a/./b/../../c/"
print(solution.simplifyPath(path))  # Output: "/c"


# class Solution:
#     def simplifyPath(self, path: str) -> str:
#         stack = []
#         res = ""
        
#         i = 0
#         while i < len(path):
#             if path[i] == '/':
#                 i += 1
#                 continue
            
#             temp = ""
#             # Iterate till we traverse the whole string and encounter the next '/'
#             while i < len(path) and path[i] != '/':
#                 temp += path[i]
#                 i += 1
            
#             if temp == ".":
#                 continue
#             elif temp == "..":
#                 if stack:
#                     stack.pop()
#             else:
#                 stack.append(temp)
        
#         # Adding all the stack elements to result
#         while stack:
#             res = "/" + stack.pop() + res
        
#         # If no directory or file is present
#         if not res:
#             return "/"
        
#         return res


