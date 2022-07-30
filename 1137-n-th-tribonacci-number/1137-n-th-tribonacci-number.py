class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        one, two, three = 0, 1, 1 
        for i in range(3, n + 1):
            one, two, three = two, three, one + two + three
            
        
        return three

        
        
        