class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        """

        """
        sumDigits = defaultdict(list)
        def calculateSumOfDigits(num):
            counter = 0
            while num:
                counter += num %10
                num //= 10
            return counter
        
        for num in nums:
            digitSum = calculateSumOfDigits(num)
            sumDigits[digitSum].append(num)
            if len(sumDigits[digitSum]) > 2:
                heapify(sumDigits[digitSum])
                heappop(sumDigits[digitSum])
        
        maxSum = -1
        for key, val in sumDigits.items():
            if len(val) == 2:
                maxSum = max(maxSum, sum(val))
        return maxSum
            