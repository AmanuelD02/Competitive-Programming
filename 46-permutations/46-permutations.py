class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        N = len(nums)
        nums = deque(nums)
        def permute(path):
            if len(path) == N:
                result.append(path.copy())
                return
            
            for i in range(N - len(path)):
                path.append(nums.popleft())
                
                permute(path)
                
                nums.append(path.pop())
                
                
        permute([])
        return result
        