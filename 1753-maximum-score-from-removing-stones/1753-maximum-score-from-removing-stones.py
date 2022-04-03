class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        heap = [-a,-b,-c]
        heapify(heap)
        ans = 0
        while len(heap) >=2:
            l1 , l2 = -1 *heappop(heap) , -1 * heappop(heap)
            ans += 1
            l1-=1
            l2-=1
            
            if l1!=0:
                heappush(heap, -l1)
            if l2 !=0:
                heappush(heap,-l2)
        return ans
            
        
        