class Solution:
    def divide(self, a: int, b: int) -> int:
        if a == -2147483648 and b == -1: 
            return 2147483647
        
        dividend, divisor, quotient = abs(a), abs(b), 0
        
        for x in reversed(range(32)):
            if (dividend >> x) - divisor >= 0:    
                quotient += 1 << x
                dividend -= divisor << x
                
        return quotient if (a > 0) == (b > 0) else -quotient
                    