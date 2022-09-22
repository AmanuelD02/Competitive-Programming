class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        paired, visited = set(), set()
        nums.sort()
        total = 0
        for num in nums:
            if num - k not in paired and num -k in visited:
                total += 1
                paired.add(num - k)
            visited.add(num)
        
        return total