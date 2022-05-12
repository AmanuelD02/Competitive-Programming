class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        N = len(nums)
        nums = deque(nums)
        print(N)
        def permute(start, path):
            if len(path) == N:
                result.append(path.copy())
                return
            
            for i in range(N - len(path)):
                path.append(nums.popleft())
                
                permute(i+1, path)
                
                nums.append(path.pop())
                
                
        permute(0, [])
        return result
        