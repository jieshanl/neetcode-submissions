class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Use the stack algorithm to track indices of unmatched opening parentheses for later removal
        # stack: [ ):(, ]:[, }:{ ]
        # remove the invalid parentheses, or the parantheses without a matching paranthese

        # first, we need to convert the string into a list so we could iterate
        string = list(s)
        stack = [] # initialize a stack array to push and pop from

        # iterate through the string array
        for i, c in enumerate(string):
            if c == '(': # if char is an open paratheses, we push its index into stack
                stack.append(i)
            elif c == ')':
                # before you pop, check if stack is empty or not
                if stack:
                    stack.pop()
                else:
                    string[i] = '' #remove it by setting string[i] to empty
        
        while stack:
            string[stack.pop()] = ''
        return ''.join(string)
                


        

        