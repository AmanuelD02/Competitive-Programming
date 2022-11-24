class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        lst = deque()
        for i in range(len(arr)):
            tmp = arr[i]
            if lst:
                arr[i] = lst.popleft()
                lst.append(tmp)
            if tmp == 0:
                lst.append(0)
    
            
                
                