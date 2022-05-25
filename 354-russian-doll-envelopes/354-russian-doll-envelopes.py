class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # print(envelopes)
        # print(self.next_index(envelopes, 0))
        
       
        N, size = len(envelopes), 1
        arr = [float("inf")] * N 
        arr[0] =  envelopes[0][1]
        for i in range(1, N):
            left = self.binarySearch(arr, envelopes[i][1])
            arr[left] = envelopes[i][1]
            if left == size:
                size += 1
        
        return size
    
    
    
    
    
    def binarySearch(self, arr, num):
        left, right = 0, len(arr) - 1
        # print(arr, left, right)
        while left < right:
            mid = (left + right) >> 1
            if arr[mid] < num:
                left = mid + 1
            else:
                right = mid
        return left