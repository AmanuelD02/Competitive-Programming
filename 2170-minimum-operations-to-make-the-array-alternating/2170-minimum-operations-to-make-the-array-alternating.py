class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1 : return 0
        
        odd, even = defaultdict(int) , defaultdict(int)
        for i, j in enumerate(nums):
            if i %2 ==0:
                even[j] += 1
            else:
                odd[j] += 1
        
        odd[-1] = 0
        even[-1] = 0
        even = sorted(even.items(), key = lambda x:x[1], reverse = True)
        odd = sorted(odd.items(), key = lambda x:x[1], reverse = True)
        
        if even[0][0] != odd[0][0]:
            return len(nums) - (even[0][1] + odd[0][1])
        
        e, o = even[0][1] + odd[1][1] , even[1][1] + odd[0][1]
        
        return len(nums) - max(e, o)