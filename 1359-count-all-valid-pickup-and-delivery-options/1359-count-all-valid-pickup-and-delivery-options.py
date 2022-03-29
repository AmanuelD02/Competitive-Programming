class Solution:
    def countOrders(self, n: int) -> int:
        fact = ans = c = 1
    
        for i in range(1,n+1):
            ans *= c
            c += 2

        for i in range(1,n+1):
            fact *= i
        
        return (fact * ans) % ((10**9) + 7)
            