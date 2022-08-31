class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        a = self.sortTopoligically(rowConditions, k)
        b = self.sortTopoligically(colConditions, k)
        if len(a) < k or len(b) <k:
            return []
        
        nums = [ [0]*k for x in range(k)]
        for i in range(k):
            for j in range(k):
                if a[i] == b[j]:
                    nums[i][j] = a[i]
        
        return nums
        

    
    def sortTopoligically(self, rowConditions, k):
        graph, queue,in_degree = defaultdict(set), deque(), defaultdict(int)
        for a,b in rowConditions:
            if b not in graph[a]:
                in_degree[b] += 1
            graph[a].add(b)

        for i in range(1,k+1):
            if in_degree[i] == 0:
                queue.append(i)
        rowSeq = []
        while queue:
            cur = queue.popleft()
            rowSeq.append(cur)
            for neigh in graph[cur]:
                in_degree[neigh] -= 1
                if in_degree[neigh] == 0:
                    queue.append(neigh)
        return rowSeq

                    
            
            