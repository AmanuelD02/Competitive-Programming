# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return ""
        
        stack = [root]
        answer = []
        while stack:
            node = stack.pop()
            if node:
                answer.append(str(node.val))
                stack.append(node.right)
                stack.append(node.left)
                
            else:
                answer.append("#")
        
        return ",".join(answer)
    
    def deserialize(self, data):
        if len(data) == 0:
            return None
        nodes = data.split(',')
        root, _  = self.helper(nodes, 0)
        
        return root
        
    def helper(self, data, i):
        if i >= len(data):
            return
        if data[i] == "#":
            return (None, i)
        
        root = TreeNode(int(data[i]))
        left, index = self.helper(data, i + 1)
        right, index = self.helper(data, index + 1)
        
        root.left = left
        root.right = right
        
        return (root, index)
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))