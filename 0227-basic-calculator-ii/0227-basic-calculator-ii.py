class Solution:
    def calculate(self, s: str) -> int:
        stack  = self.stringToStack(s)
        
        
        postfix = self.convertToPostFix(stack)
        res = self.evaluatePostFix(postfix)
        
        return res

        
    def stringToStack(self, s: str) -> List:
        stack, nums = [], []
        
        for i in s:
            if i.isdigit():
                nums.append(i)
            else:
                if nums:
                    stack.append(int("".join(nums)))
                    
                if i != ' ':
                    stack.append(i)
                
                nums = []
        
        
        if nums:
            stack.append(int("".join(nums)))
        
        return stack

        
    def convertToPostFix(self, stack):
        ops = {"+", "-", "*", "/"}
        resultStack, postFix = [], []
        precedence = {}
        
        precedence['/'] =  precedence['*'] = 4
        precedence['+'] =  precedence['-'] = 2
        
        for i, curr in enumerate(stack):
            if str(curr) in ops:
                while postFix and precedence[postFix[-1]] >= precedence[curr]:
                    resultStack.append(postFix.pop())
            
                postFix.append(curr)
            else:
                resultStack.append(curr)
                
        postFix.reverse()
        return resultStack + postFix
    
    
    def evaluate(self, num1,num2, operator):
        return int(eval(str(num1) + operator + str(num2)))
                
    
    def evaluatePostFix(self, stack):
        ops = {"+", "-", "*", "/"}
        resultStack = []
        
        for curr in stack:
            if curr in ops:
                num1 = resultStack.pop()
                num2 = resultStack.pop()
                
                res  = self.evaluate(num2, num1, curr)
                
                resultStack.append(res)
                
            else:
                resultStack.append(curr)
        
        return resultStack.pop()
        
        