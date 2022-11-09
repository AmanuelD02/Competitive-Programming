class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        frequency = Counter(nums)
            # repitied, missing
        answer = [None, None]
        for num in range(1, n + 1):
            freq = frequency[num]
            
            if freq ==2:
                answer[0] = num
            if freq == 0:
                answer[1] = num
            
            if answer[0] and answer[1]:
                break
        
        return answer
            