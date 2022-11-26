class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        moves = 0
        
        for p in s:
            if p =="(":
                stack.append("(")
            elif stack:
                stack.pop()
            else:
                moves += 1
        
        return len(stack) + moves