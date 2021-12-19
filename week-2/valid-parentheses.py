class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = {"(":1, "{":2, "[":3 }
        closing = closing = {")":1, "}":2, "]":3}
        
        for i in s:
            if i in opening:
                stack.append(i)
            else:
                if stack ==[]:
                    return False
                top = stack.pop()
                if opening[top] != closing[i]:
                    return False
        
        return stack == []
                
        