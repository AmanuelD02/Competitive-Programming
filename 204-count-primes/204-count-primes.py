class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True] * n
        count = 0       
        for i in range(2,n):
            if primes[i]:
                j = i
                count += 1
                while j*i < n:
                    primes[j*i] = False
                    j += 1
                    
        return count

        

        
        