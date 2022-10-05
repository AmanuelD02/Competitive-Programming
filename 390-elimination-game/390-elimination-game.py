class Solution:
    def lastRemaining(self, n: int) -> int:
        direction = True # --> true <-- False
        head = step = 1
        while n >1:
            if direction:
               head += step
            else:
                head += step if n%2 else 0
            
            n//=2
            step*=2
            direction = not direction
        
        return head