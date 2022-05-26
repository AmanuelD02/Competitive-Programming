class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0]
        for i in range(n):
            ans.extend([ ((1<<i) + x) for x in reversed(ans)])
        return ans