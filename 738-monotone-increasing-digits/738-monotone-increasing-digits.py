class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        
        stack = list(str(n))
        FLAG = False
        for i in range(len(stack) -1):
            if stack[i] > stack[i + 1]: 
                FLAG = True
                break
        if FLAG:
            for j in range(i + 1, len(stack)):
                stack[j] = '9'
        
            stack[i] = str(int(stack[i]) - 1)
            for i in range(i, 0,-1):
                if stack[i] < stack[i-1]:
                    stack[i] = '9'
                    stack[i-1] = str(int(stack[i-1]) - 1)
                else:
                    break
        
            return int("".join(stack))
        else:
            return n
                
        
        