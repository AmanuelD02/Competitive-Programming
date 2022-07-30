class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i in range(len(mat)):
            row = sum(mat[i])
            heappush(heap, (-row, -i))
            if len(heap) >k:
                heappop(heap)
        
        ans = []
        while heap:
            ans.append( -heappop(heap)[1])
        
        return ans[::-1]