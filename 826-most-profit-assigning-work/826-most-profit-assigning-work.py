class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        D, W = len(difficulty), len(worker)
        jobs  = sorted(zip(difficulty, profit))
    
        i = best = total_profit = 0
        for work in sorted(worker):
            while i < D and jobs[i][0] <= work:
                best = max(best, jobs[i][1])
                i += 1
            total_profit += best
            
        
        return total_profit
                
        
        