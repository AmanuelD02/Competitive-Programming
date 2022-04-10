class Solution:
    def calPoints(self, ops: List[str]) -> int:
        totalSum = 0
        stack = []
        
        for op in ops:
            if op.isdigit() or op[1:].isdigit():
                stack.append(int(op))
                totalSum += int(op)
            elif op == "C":
                totalSum -= stack.pop()
            elif op == "D":
                stack.append(2 * stack[-1] )
                totalSum += stack[-1]
            else:
                stack.append(stack[-1] + stack[-2])
                totalSum += stack[-1]
        
        
        return totalSum
                