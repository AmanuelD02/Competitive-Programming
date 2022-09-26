class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        D, W = len(difficulty), len(worker)
        mult  = [(difficulty[x],profit[x]) for x in range(D)]
        mult.sort()
    
        def bisect_right(ability):
            lo, hi = 0, D
            while lo < hi:
                mid = lo + (hi -lo)//2
                if mult[mid][0] > ability: hi = mid
                else: lo = mid + 1
            return lo
        
        total_profit = 0
        cur_max = [0]
        for d,p in mult:
            cur_max.append(max(cur_max[-1], p))
            
        for w in worker:
            ability = bisect_right(w)
            if ability==0: continue
            total_profit += cur_max[ability]
        
        return total_profit
                
        
        