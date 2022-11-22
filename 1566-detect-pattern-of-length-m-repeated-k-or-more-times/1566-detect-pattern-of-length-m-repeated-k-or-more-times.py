class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        N = len(arr)
        
        if N < m or N < k:
            return False
        

        left, right = 0, m - 1 
        startLeft, startRight = 0, m - 1
        count = 0
        while right < N:
            if arr[startLeft: startRight + 1] == arr[left: right + 1]:
                count += 1
                
                if count >= k:
                    return True
                
                left += m
                right += m
            else:
                startLeft += 1
                startRight += 1
                left, right = startLeft, startRight
                count = 0
        
        return False
                