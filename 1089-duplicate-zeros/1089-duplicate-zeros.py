class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        N  = len(arr)
        shifts = arr.count(0)
        
        for i in range(N-1, -1, -1):
            if arr[i] != 0:
                if i + shifts < N:
                    arr[i + shifts] = arr[i] 
            if arr[i] == 0:
                if i + shifts < N:
                    arr[i + shifts] = arr[i] 
                shifts -= 1
                if i + shifts < N:
                    arr[i + shifts] = arr[i] 

                
                