class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        left, right = 0, len(s)
        ans = []
        for i in s:
            if i=="I":
                ans.append(left)
                left += 1
            else:
                ans.append(right)
                right -= 1
        ans.append(left)
        return ans
                
        
            