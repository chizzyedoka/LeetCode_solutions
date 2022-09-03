class Stack:
            def __init__(self):
                self.data = []
            def push(self,item):
                self.data.append(item)
            def pop(self):
                return self.data.pop()
            def top_item(self):
                return self.data[-1]
            def size(self):
                return len(self.data)
class Solution:
    def isValid(self, s: str) -> bool:        
        mystack = Stack()
        parenthesis = {'(':')',
                       '{':'}',
                       '[':']'
                      }
        for i in s:
            if i in parenthesis.keys(): # open parenthesis
                mystack.push(i)
            elif i not in parenthesis.keys(): # closed parenthesis
                if mystack.size() == 0: #no open parenthesis
                    return False
                open_brackets = mystack.pop()
                if i != parenthesis[open_brackets]:
                    return False
        return mystack.size() == 0
                
        