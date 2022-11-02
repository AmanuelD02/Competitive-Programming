class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        reminders = [0] * k
        reminders[0] = 1
        curSum = answer = 0 

        for num in nums:
            curSum = (curSum + num) % k
            answer += reminders[curSum]
            reminders[curSum] += 1
        
        return answer