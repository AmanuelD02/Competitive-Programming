class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        N = len(nums)
        unique = collections.Counter(nums)
        def permutation(path):
            if len(path) == N:
                result.append(path.copy())
                return
            
            for num in unique:
                if unique[num]:
                    unique[num] -= 1
                    path.append(num)
                    permutation(path)
                    unique[num] += 1
                    path.pop()
        
        permutation([])
        return result
                    