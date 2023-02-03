# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        graph = defaultdict(list) 
        queue = deque([(root,0)])
        
        while queue:    
            temp = defaultdict(list)
            for i in range(len(queue)):
                node, s = queue.popleft()
                
                temp[s].append(node.val) 
                if node.left:
                    queue.append((node.left, s-1)) 
                if node.right:
                    queue.append((node.right,s+1))
            
            for i in temp:
                graph[i].extend(sorted(temp[i]))

        return [graph[i] for i in sorted(graph)]