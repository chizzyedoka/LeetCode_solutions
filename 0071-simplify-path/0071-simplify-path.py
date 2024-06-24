# class Solution:
#     def simplifyPath(self, path: str) -> str:
#         # Split the path by '/' to handle each component
#         components = path.split('/')
#         stack = []

#         for component in components:
#             if component == '' or component == '.':
#                 # Ignore empty components and current directory references
#                 continue
#             elif component == '..':
#                 # Pop from the stack if there is a previous directory
#                 if stack:
#                     stack.pop()
#             else:
#                 # Push the directory name onto the stack
#                 stack.append(component)

#         # Join the stack elements with '/' to form the simplified path
#         return '/' + '/'.join(stack)



class Solution:
    def simplifyPath(self, path):
        stack = []
        for elem in path.split("/"):
            if stack and elem == "..":
                stack.pop()
            elif elem not in [".", "", ".."]:
                stack.append(elem)
                
        return "/" + "/".join(stack)


