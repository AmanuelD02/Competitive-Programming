import heapq as hq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.lst = nums
        self.k = k
        heapify(self.lst)
        for i in range(len(self.lst) - k):
            heappop(self.lst)

            
        

    def add(self, val: int) -> int:
        if  len(self.lst)<=self.k or val >self.lst[0] :
            heappush(self.lst,val)
        for i in range(len(self.lst) - self.k):
            heappop(self.lst)
        return self.lst[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)