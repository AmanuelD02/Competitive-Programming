class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        stamp = [x for x in stamp]
        target = [x for x in target]
        def canReplace(start):
            for i in range(start,start + len(stamp)):
                if not(target[i] == '?' or target[i] ==stamp[ (i-start)]):
                    return False
            return True
        
        def replace(start):
            count = 0
            for i in range(start, start + len(stamp)):
                if target[i] != '?':
                    count += 1
                    target[i] ='?'
            return count
        
        ans = []
        count = 0
        T = len(target)
        visited = [False] * T
        
        while count < T:
            didChange = False
            for i in range(T-len(stamp)+1):
                if not visited[i] and canReplace(i):
                    visited[i] = True
                    count += replace(i)
                    didChange = True
                    ans.append(i)
            if not didChange:
                return []
        
        
        return ans[::-1]