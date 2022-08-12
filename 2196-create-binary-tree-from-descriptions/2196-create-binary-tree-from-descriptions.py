# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        tree = defaultdict(TreeNode)
        isNotRoot = set()
        for node, child, isLeft in descriptions:
            cur = tree[node]
            cur.val = node
            
            tree[child].val = child
            isNotRoot.add(child)
            if isLeft:
                cur.left = tree[child]
            else:
                cur.right = tree[child]
        
        for val, node in tree.items():
            if val not in isNotRoot:
                return node
        
        
        