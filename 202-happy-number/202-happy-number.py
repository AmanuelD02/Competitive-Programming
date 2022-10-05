class Solution:
    def isHappy(self, n: int) -> bool:
        if n ==1: return True
        store = set()
        while True:
            if n in store: break
            if n==1: break
            store.add(n)
            sums = 0
            while n >0:
                sums += (n%10)**2
                n = n//10
            n = sums
        
        return n == 1
        