class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        farmed = [float("inf")] * len(nums)
        for num in nums:
            indx = self.binary_search(farmed, num)
            farmed[indx] = num

        k = 0
        for num in farmed:
            if num == float("inf"):
                break
            k += 1
        
        return k >= 3
    
    def binary_search(self, farmed, num):
        left, right = 0, len(farmed)
        while left <= right:
            mid = (left + right) // 2
            if farmed[mid] >= num:
                right = mid - 1
            else:
                left = mid + 1
        return left
            