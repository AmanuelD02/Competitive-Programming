class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr)<=1: return 0
        
        graph = defaultdict(list)
        for i, j in enumerate(arr):
            graph[j].append(i)
            
        visited, step, queue = set([0]) , 0, deque([0])
        
        while queue:
            for i in range(len(queue)):

                position = queue.popleft()
                if position == len(arr) -1: return step
                
                for c in graph[arr[position]]:
                    if c not in visited:
                        visited.add(c)
                        queue.append(c)
                
                graph[arr[position]].clear()
                
                for child in [position -1, position +1]:
                    if 0<= child < len(arr) and child not in visited:
                        visited.add(child)
                        queue.append(child)
                        
            step +=1
            
        return -1
                        
        