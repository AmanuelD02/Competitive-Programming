class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        cands = [2, 3, 5]
        curPicked = [2]
        ans = []
        
        """
      
        ans = []
        candidates.sort()
        def recur(start, curSum, picked):
            if curSum == target:
                ans.append(picked[:])
                return

            
            for i in range(start, len(candidates)):
                if curSum + candidates[i] <=target:
                    picked.append(candidates[i])
                    curSum += candidates[i]
                    
                    recur(i,curSum, picked)
                    
                    picked.pop()
                    curSum -= candidates[i]
                else:
                    break
                

            
        
        recur(0,0,[])
        return ans
                
            