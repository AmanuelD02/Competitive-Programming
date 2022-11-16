class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        output = []
        heap = []
        for i in range(min(k, len(nums1))):
            heappush(heap, [nums1[i] + nums2[0], nums1[i], 0 ])
        
        
        for _ in range(k):
            if not heap: break
            _, n1, idx = heappop(heap)
            output.append([n1, nums2[idx]])
            if idx + 1 < len(nums2):
                heappush(heap, [ n1 + nums2[idx + 1], n1, idx + 1 ])
        
        
        return output
                
            