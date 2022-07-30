class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1, stack2 = [], []
        for i in s:
            if i =="#" and stack1:
                stack1.pop()
            elif i!="#":
                stack1.append(i)
        for j in t:
            if j =="#" and stack2:
                stack2.pop()
            elif j!="#":
                stack2.append(j)
        return stack1 == stack2
            
        