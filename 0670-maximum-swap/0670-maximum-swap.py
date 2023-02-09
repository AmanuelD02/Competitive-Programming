class Solution:
    def maximumSwap(self, num: int) -> int:
        ans = list(str(num))
        num = list(str(num))
        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                num[i], num[j] = num[j], num[i]
                ans = max(ans, num[:])
                
                num[i], num[j] = num[j], num[i]
                
        
        
        
        
        
        return int("".join(ans))