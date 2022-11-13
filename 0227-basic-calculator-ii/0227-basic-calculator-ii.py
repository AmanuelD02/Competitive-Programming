class Solution:
    
    def evaluate(self, num1, num2, ops):
        return eval(str(num1) + ops + str(num2))
    
    def convert(self, stack, ops):
        newStack = []
        i = 0
        while i < len(stack):
            if str(stack[i]) in ops:
                num1 = newStack.pop()
                num2 = stack[i + 1]
                
                res = self.evaluate(num1, num2, stack[i])
                newStack.append(int(res))
                i += 1
            else:
                newStack.append(stack[i])
            
            i += 1
                
        return newStack
    
    def calculate(self, s: str) -> int:
        stack = []
        nums = []
        
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
        
        
        newStack = self.convert(stack[:], "*/")
        newStack2 = self.convert(newStack[:], "+-")
        
        return int(newStack2.pop())
        


        
        
        