class Solution:
    def reorganizeString(self, s: str) -> str:
        prev, freq = None, Counter(s)
        letters = []
        max_heap = [(-val, key) for key, val in freq.items()]
        heapq.heapify(max_heap)
        while max_heap:
            count, val = heappop(max_heap)
            letters.append(val)
            count += 1
            
            if prev:
                if prev[0] < 0:
                    heappush(max_heap, prev)
                prev = None
            
            if count < 0:
                prev = (count, val)
        
        
        return "".join(letters) if not prev else ""