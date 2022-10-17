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
        nodes = {}
        visited = set()
        def dfs(node):
            if not node:
                return
            visited.add(node)
            if node not in nodes:
                nodes[node] = Node(node.val)
            cur_copy = nodes[node]
            
            for neigh in node.neighbors:
                if neigh not in nodes:
                    nodes[neigh] = Node(neigh.val)
                cur_copy.neighbors.append(nodes[neigh])
                if neigh not in visited:
                    dfs(neigh)
        
        dfs(start)
        return nodes[start]

            

                
        