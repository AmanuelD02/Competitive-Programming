class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        XOR = 0
        for n in nums:
            XOR ^= n
        
        # differ at
        differ = 1

        while not (XOR & 1):
            differ <<= 1
            XOR >>= 1

        ans = [0, 0]
        
        for num in nums:
            if differ & num:
                ans[0] ^= num
            else:
                ans[1] ^= num
        
        
        return ans