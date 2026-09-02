class Solution:
    def isValid(self, s: str) -> bool:
        # ([)]
        # [ ([  )]  ]
        # HAVE a stack
        # loop through the string
        # has long as we have an open paranthesis, put in the stack
        # when we have a closed parenthesis, if the top of the stack is not a match return false
        # if we get to the end of the loop, return true
        if not s:
            return True
        stack = []
        parenthesis = {
            '(':')',
            '[':']',
            '{':'}'
        }
        for i in s:
            if i in parenthesis:
                stack.append(i)
            else:
                if not stack:
                    return False
                if stack:
                    top = stack.pop()
                    if parenthesis[top] != i:
                        return False
        return len(stack) == 0
