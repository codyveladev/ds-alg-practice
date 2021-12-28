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
            #Append the open bracket to the stack 
            if char in openBrackets: 
                stack.append(char)
            elif char in closedBrackets: 
                #If we come across a closed bracket with no items on stack 
                #then the string cannot be a valid parentheses 
                if len(stack) == 0: 
                    return False 
                #If the last item in our stack is the matching pair for the current bracket
                #Remove the open bracket off of the stack
                if stack[-1] == bracketPairs[char]: 
                    stack.pop()
                else: 
                    #If we run into another case 
                    #Return false 
                    return False 
        #If we have items on the stack still then not everthing got removed 
        #So we dont have a valid parentheses as if we did everything on the stack 
        #Would have gotten a matching pair
        return len(stack) == 0 