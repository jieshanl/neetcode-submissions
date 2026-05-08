class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # we can never start with a closing parantheses
        # use the backtracking algorithm

        #               [ ]  # we start with an empty array
        #                |
        #               [(] # we can only add an open paranthese at first
        #              /    \
        #           [((]      [()]
        #           /   \       \
        #       [(((]   [(()]       [()(]
        #       /       /   \         /   \
        #   [((()]   [(()(]  [(())] [()((] [()()]
        #   /         /         /      |       \
        #  [((())]  [(()()]  [(())(] [()(()]    [()()(]
        #   |          |        |       |          \
        #  [((()))] [(()())] [(())()] [()(())]  [()()()]

        stack = [] # this is a global stack
        res = []

        # define a helper backtrack function and recursicely call it
        # rules to obey: open count > close count if we wanna add a close paranthese
        # open count < n
        def backtrack(openN, closeN): # we pass in open count and close count variables
            # base case: 
            if openN == closeN == n:
                res.append("".join(stack))
                return # break out of this function since we've found the solution
            
            # recursive case if openN < n
            if openN < n:
                stack.append("(") # we wanna append ( to stack
                backtrack(openN + 1, closeN)
                # pop from the stack so we can traverse the other decision
                stack.pop()
            
            # another recursive case when if closeN < openN
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
            
        backtrack(0, 0) # call the backtrack function and start with an empty stack with both counts 0
        return res









