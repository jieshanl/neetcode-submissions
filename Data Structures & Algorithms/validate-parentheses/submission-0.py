class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"]" : "[", ")" : "(", "}" : "{"} # our hashmap to map the correct type

        for c in s:
            if c in closeToOpen: # A key in closeToOpen or a closing paranthesis
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else: # Open paranthesis case, just keep appending into stack
                stack.append(c)
        
        return True if not stack else False # return true only if stack is empty
