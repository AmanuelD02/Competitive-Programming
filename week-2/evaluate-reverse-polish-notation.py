class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        ops = "/+-*"
        for i in tokens:
            if i in ops:
                a = stack.pop()
                b = stack.pop()
                result  = int(eval(str(b) + i + str(a)))
                stack.append(result)
            else:
                stack.append(i)
        return stack.pop()
        