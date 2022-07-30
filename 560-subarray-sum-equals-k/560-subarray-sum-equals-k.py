class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefix_freq = defaultdict(int)
        prefix_freq[0] = 1
        prefix = 0
        for i in nums:
            prefix += i
            result += prefix_freq[prefix - k]
            prefix_freq[prefix] += 1
        return result