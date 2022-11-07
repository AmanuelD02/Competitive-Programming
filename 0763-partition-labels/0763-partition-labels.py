class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        rightMost = defaultdict(int)
        
        for i, char in enumerate(s):
            rightMost[char] = i
            
        partition = []
        furthest = rightMost[s[0]]
        prev = -1
        
        for i in range(n):
            furthest = max(furthest, rightMost[s[i]])
            if furthest <= i:
                partition.append(i - prev)
                prev = i
        
        return partition