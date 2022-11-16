class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        output = []
        heap = []
        n, m = len(nums1), len(nums2)
        visited = {(0, 0)}
        if not nums1 or not nums2:
            return
        heappush(heap, [nums1[0] + nums2[0],  nums1[0], nums2[0], 0, 0 ])
        for _ in range(k):
            if not heap: break
            _, n1, n2, id1, id2 = heappop(heap)
            output.append([n1, n2])
            
            if id1 + 1 < n and (id1 + 1, id2) not in visited:
                heappush(heap, [nums1[id1 + 1] + nums2[id2],nums1[id1 + 1], nums2[id2], id1 + 1, id2]  )
                visited.add((id1 + 1, id2))
                
            if id2 + 1 < m and (id1, id2 + 1) not in visited:
                heappush(heap, [nums1[id1] + nums2[id2 + 1],nums1[id1], nums2[id2 + 1], id1, id2 + 1 ])
                visited.add((id1, id2 + 1))
        return output