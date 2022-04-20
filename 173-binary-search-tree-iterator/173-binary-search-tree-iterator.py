# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.elements = []
        self.current = 0
        def inorder(node):
            if node:
                inorder(node.left)
                self.elements.append(node.val)
                inorder(node.right)
        inorder(root)

    def next(self) -> int:
        cur = self.elements[self.current]
        self.current +=1 
        return cur

    def hasNext(self) -> bool:
        return self.current < len(self.elements)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()