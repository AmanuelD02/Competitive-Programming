class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        best = [-1,-1]
        def helper(lowest):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left + right) //2
                if nums[mid] == target:
                    if lowest:
                        best[0] = mid
                        right = mid - 1
                    else:
                        best[1] = mid
                        left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        
     
        helper(True)
        helper(False)
        return best
                
    