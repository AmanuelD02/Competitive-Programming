class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = []
        for i in range(len(mat)):
            row = sum( mat[i])
            arr.append((row, i) )
        arr.sort()
        
        ans = []
        for i in range(k):
            ans.append(arr[i][1])
        
        return ans