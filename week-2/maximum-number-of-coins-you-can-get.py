class Solution:
    def maxCoins(self, piles) -> int:
        piles.sort()
        me = len(piles) -2
        bob = 0
        total = 0
        while(me >bob):
            total += piles[me]
            me-=2
            bob +=1
        return total
            
        