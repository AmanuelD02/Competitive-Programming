"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, start: 'Node') -> 'Node':
        if not start: return
        queue, clones = deque([start]), {start: Node(start.val)}
        while queue:
            cur = queue.popleft()
            cur_clone = clones[cur]
            
            for neigh in cur.neighbors:
                if neigh not  in clones:
                    queue.append(neigh)
                    clones[neigh] = Node(neigh.val)
                
                cur_clone.neighbors.append(clones[neigh])
        
        
        return clones[start]

                
        