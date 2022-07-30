class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.extend([0,h])
        verticalCuts.extend([0, w])
        horizontalCuts.sort()
        verticalCuts.sort()
        v_max = h_max = 0
        for i in range(len(horizontalCuts)-1):
            h_max = max(h_max, horizontalCuts[i + 1] - horizontalCuts[i])
        for j in range(len(verticalCuts) - 1):
            v_max = max(v_max, verticalCuts[j+1] - verticalCuts[j])
        
        return (h_max * v_max) % (10**9 + 7)