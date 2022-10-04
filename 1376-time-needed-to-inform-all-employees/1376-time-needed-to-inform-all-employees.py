class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph, queue = defaultdict(set), deque()
        for i, head in enumerate(manager):
            graph[head].add(i)
        
        queue.append((headID,informTime[headID]))
        total_time = 0
        while queue:
            for i in range(len(queue)):
                curEmp, curTime = queue.popleft()    
                for subEmp in graph[curEmp]:
                    total_time = max(total_time, informTime[subEmp] + curTime ) 
                    queue.append((subEmp,informTime[subEmp] + curTime))
        
        return total_time
                
        
        