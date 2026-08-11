class Solution:
    def isValid(self, s: str) -> bool:
        # first we will check is string is empty
        if len(s) == 0:
            return True
        # We will check if the len of char is odd, if odd then we can return False right away
        elif len(s) % 2 != 0:
            return False
        # We need a stack to push elements 
        stack = []
        mapping = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        
        for char in s: 
            # we will check is char("(") is in the below collection 
            if char in ("(","{","["):
                stack.append(char)
            elif len(stack) == 0:
                return False
            elif stack[-1] != mapping[char]:
                return False

            else:
                stack.pop()
        return not stack

            
        