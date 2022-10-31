class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part = list(part)
        for char in s:
            stack.append(char)
            if len(stack) >= len(part):
                if stack[-len(part):] == part:
                    for _ in range(len(part)):
                        stack.pop()
        
        return "".join(stack)