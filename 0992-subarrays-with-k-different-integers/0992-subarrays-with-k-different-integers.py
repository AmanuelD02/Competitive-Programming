class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def niceSubarray(arr, k):
            left =  right =  nice  = 0
            freq = defaultdict(int)
            
            while right < len(arr):
                freq[arr[right]] += 1
                
                while len(freq) > k:
                    freq[arr[left]] -= 1
                    
                    if freq[arr[left]] == 0:
                        del freq[arr[left]]
                        
                    left += 1
                right += 1
                
                nice += right - left
                
            return nice
        
        return niceSubarray(nums, k) - niceSubarray(nums, k - 1)
                        
        