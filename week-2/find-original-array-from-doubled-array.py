from typing import *
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) %2 ==1:
            return []
        changed.sort()
        visited = {}
        lst = []
        for i in range(len(changed)):
            if changed[i]/2 in visited:

                lst.append(int(changed[i]/2))
                visited[int(changed[i]/2)] -=1
                if visited[int(changed[i]/2)] ==0:
                    visited.pop(int(changed[i]/2))
                
                    
                    
            else:
                if visited.get(changed[i]):
                    visited[changed[i]] +=1
                else:
                    visited[changed[i]] = 1
                            
        if len(changed)/2 == len(lst):
            
            return lst
        return []