class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def counter(num):
            c = defaultdict(int)
            for i in num:
                c[int(i)] += 1
     
            return (c[0], c[1])
        
        arr = []
        for i in strs:
            arr.append(counter(i))
            
        @lru_cache(None)
        def dp(i, mr, nr):
            if i >= len(arr):
                return 0
            
            pick = 0
            if mr - arr[i][0] >= 0 and nr - arr[i][1] >= 0:
                pick = 1 + dp(i + 1, mr - arr[i][0], nr - arr[i][1])
            
            not_pick = dp(i + 1, mr, nr)
            
            return max(pick, not_pick)
        
        return dp(0, m , n)