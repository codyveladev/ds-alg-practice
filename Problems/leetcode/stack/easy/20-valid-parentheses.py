class Solution:
    def isValid(self, s: str) -> bool:
        bracketPairs = {
            ']': '[', 
            '}': '{', 
            ')': '('
        }
        openBrackets = '{[('
        closedBrackets = ')]}'
        stack = []
        for char in s: 
            if char in openBrackets: 
                stack.append(char)
            elif char in closedBrackets: 
                if len(stack) == 0: 
                    return False 
                if stack[-1] == bracketPairs[char]: 
                    stack.pop()
                else: 
                    return False 
        return len(stack) == 0 