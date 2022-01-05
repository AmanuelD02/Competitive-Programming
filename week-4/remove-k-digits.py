# https://leetcode.com/problems/remove-k-digits/
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if k ==  len(num):
            return '0'
        
        lst = [x for x in num]
        stack = []
        
        for i in lst:
            while stack and stack[-1] > i and k >0: 
                stack.pop()
                k-=1                
            stack.append(i)
        while(k >0):
            stack.pop()
            k-=1
        return str(int(''.join(stack)))
        
        