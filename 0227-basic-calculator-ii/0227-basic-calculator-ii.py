class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        N = len(s)
        stack, curNum = [], []
        ops = "+-*/"
        i, sign = 0, 1
        
        while i < N:
            curr = s[i]

            if curr not in ops:
                curNum.append(curr)
            elif curr == "+" or curr == "-":
                num1 = sign * int("".join(curNum)) if curNum else stack.pop()
                stack.append(num1)
                curNum = []
                sign = -1 if curr == "-" else 1
            elif curr == "*" or curr =="/":
                num1 = sign * int("".join(curNum)) if curNum else stack.pop()
                sign  = 1
                curNum = []
                i+= 1
                while i < N and s[i].isdigit():
                    curNum.append(s[i])
                    i += 1
                num2 = int("".join(curNum))
                if curr == "*":
                    stack.append(num1*num2)
                else:
                    stack.append(int(num1/num2))
                curNum = []
                i -= 1
            i += 1
        # print(stack, curNum, sign)
        if curNum:
            stack.append(sign * int("".join(curNum)))
        return sum(stack)
            
                
        