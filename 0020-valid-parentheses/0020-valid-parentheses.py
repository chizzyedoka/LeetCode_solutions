class Stack:
    def __init__(self):
        self.arr = []
    def push(self,value):
        self.arr.append(value)
    def pop(self):
        return self.arr.pop()
    def length(self):
        return len(self.arr)
    def peek(self):
        return sel.arr[-1]
    def print_out(self):
        print(self.arr)
        
        
class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        parenthesis = {
            '(':')',
            '{':'}',
            '[':']'
        }
        for p in s:
            if p in parenthesis.keys():
                stack.push(p) #open parenthesis are in stack
            elif p not in parenthesis.keys():
                if stack.length() == 0:
                    return False
                openBracket = stack.pop()
                if p != parenthesis[openBracket]:
                    return False
        return stack.length()==0
            
            
            
            
            
            
            

# class Solution:
#     def isValid(self, s: str) -> bool:        
#         mystack = Stack()
#         parenthesis = {'(':')',
#                        '{':'}',
#                        '[':']'
#                       }
#         for i in s:
#             if i in parenthesis.keys(): # open parenthesis
#                 mystack.push(i)
#             elif i not in parenthesis.keys(): # closed parenthesis
#                 if mystack.size() == 0: #no open parenthesis
#                     return False
#                 open_brackets = mystack.pop()
#                 if i != parenthesis[open_brackets]:
#                     return False
#         return mystack.size() == 0
        
