class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        size = 1
        N = len(nums)
                
        if N < 2:
            return nums
        
        while size < N:
            low = 0
            
            while low < N - 1:
                mid = min(N -1, low + size -1) 
                high = min(N - 1, low + (size * 2) -1)
                
                self.merge(nums, low, mid, high)
          
                low += (size * 2)
            
            size *= 2
    
        
        return nums
    
    
    def merge(self,nums, low, mid, high):
        p1 = 0
        p2 = mid + 1
        i = low
        
        tmp = nums[low: mid + 1]
        N = len(tmp)
        
        while p1 < N and p2 <= high:
            
            if tmp[p1] > nums[p2]:
                nums[i] = nums[p2]
                p2 += 1
                
            else:
                nums[i] = tmp[p1]
                p1 += 1
            
            i += 1
            
            
        while p1 < N:
            nums[i] = tmp[p1]
            p1 += 1
            i += 1
            