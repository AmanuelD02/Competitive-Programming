class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==1:
            return x
        if n ==0:
            return 1
        if n<0:
            return 1/ self.myPow(x, -n)

        if n%2 ==1:
            return x * self.myPow(x, n-1)
        else:
            p = self.myPow(x, n/2)
            return p **2
                