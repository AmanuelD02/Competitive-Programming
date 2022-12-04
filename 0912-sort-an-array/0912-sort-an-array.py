class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
                
        if N < 2:
            return nums
        
        self.sort(nums, 0 , N - 1)
    
        
        return nums
    
    
    
    def sort(self, nums, low, high):
        if low >= high:
            return
        
        mid = (low + high) //2
        
        leftSide = self.sort(nums, low, mid)
        rightSide = self.sort(nums, mid + 1, high)
        
        self.merge(nums, low, mid, high)
        
    
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
            