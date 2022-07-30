class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def combination(path, start, current_sum):
            if len(path) == k:
                if current_sum == n:
                    result.append(path.copy())
                return
            if current_sum > n:
                return
            
            for num in range(start, 10):
                path.append(num)
                current_sum += num
                combination(path, num + 1, current_sum)
                
                path.pop()
                current_sum -= num
        
        combination([], 1, 0)
        return result
                
            
            
            