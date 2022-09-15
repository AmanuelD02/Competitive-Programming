class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        store = defaultdict(int)
        ans = []
        for num in reversed(changed):
            if store[num*2] > 0:
                store[num*2] -= 1
                ans.append(num)
            else:
                store[num] += 1
        
        if len(ans)*2 != len(changed) : return []
        return ans