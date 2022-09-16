class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        no_connections = defaultdict(int)
        
        for a, b in edges:
            no_connections[a] += 1
            no_connections[b] += 1
        
        maxKey = [0,0]
        for val, key in no_connections.items():
            if key > maxKey[0]:
                maxKey = [key, val]
        
        return maxKey[1]