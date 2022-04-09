class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        heap = []
        for element, f in freq.items():
            if len(heap) < k:
                heappush(heap,(f,element))
            elif heap[0][0] < f:
                heapreplace(heap, (f,element))
        
        
        return [x[1] for x in heap]