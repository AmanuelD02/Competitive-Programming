class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = set()
        N = len(nums)
        nums = deque(nums)
        def permute(path):
            if len(path) == N:
                res = tuple(path)
                if res not in result:
                    result.add(res)
                    return
            
            for i in range(N - len(path)):
                path.append(nums.popleft())
                permute(path)
                nums.append(path.pop())
        permute([])
        return [ list(x) for x in result]