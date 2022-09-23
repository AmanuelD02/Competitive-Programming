class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        ans = 0
        for i,age in enumerate(ages):
            lb = age                                  
            ub = (age - 7) * 2                        
            i = self.helper(lb,ages)          
            j = self.helper(ub,ages)          
            if j - i <= 0: continue
            ans += j - i                      
            if lb <= age < ub:
                ans -= 1
        
        return ans
    
    def helper(self,x,a):
        lo, hi = 0, len(a)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if a[mid] < x: lo = mid + 1
            else: hi = mid
        return lo