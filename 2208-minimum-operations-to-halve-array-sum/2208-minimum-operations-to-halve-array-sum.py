class Solution:
    def halveArray(self, nums: List[int]) -> int:
        heap = []
        k = total = 0
        for i in nums:
            total += i
            heappush(heap, -1*i)
        desired = total /2
        while heap:
            if desired >= total:
                return k
            a = (-1 * heappop(heap)) /2
            total -= a
            heappush(heap, -1*a)
            k +=1
        return k
            
        
        
        