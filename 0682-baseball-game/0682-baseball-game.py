class Solution:
    def calPoints(self, arr: List[str]) -> int:
        stack = []
        ops = {"C", "D", "+"}

        for val in arr:
            if stack and val in ops:
                if len(stack) >= 2:
                    left = stack[-2]
                right = stack[-1]
                if val == "C":
                    stack.pop()
                elif val == "D":
                    stack.append(2*right)
                else:
                    stack.append(int(right) + int(left))
            else:
                stack.append(int(val))
        sum = 0
        for i in stack:
            sum += i 

        return sum
                