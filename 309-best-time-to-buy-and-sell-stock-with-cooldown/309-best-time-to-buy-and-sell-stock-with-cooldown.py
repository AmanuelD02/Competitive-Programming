class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def recur(index, state):
            if index >= len(prices):
                return 0
            if not state:
                return max(recur(index+1, not state) - prices[index],  recur(index +1, state))
            else:
                return max( recur(index+2, not state) + prices[index] , recur(index+1, state))
        
        return recur(0, False)
    