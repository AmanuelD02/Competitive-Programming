class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def combination(i, temp):
            if i == k or sum(temp) > n:
                if sum(temp) == n and sorted(temp) not in result: 
                    result.append(sorted(temp))
                return
                        
            for j in range(1,10):
                if j not in temp:
                    temp.append(j)
                    combination(i + 1, temp)
                    temp.pop()
        
        
        combination(0, [])
        return result
        
            