# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        output = [str(root.val)]
        queue = deque([root])
        while queue:
            parent = queue.popleft()
            if parent.left:
                output.append(str(parent.left.val))
                queue.append(parent.left)
            else:
                output.append("#")
            if parent.right:
                output.append(str(parent.right.val))
                queue.append(parent.right)
            else:
                output.append("#")
        # print(",".join(output))
        return ",".join(output)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if data == "": return None
        lst = data.split(",")
        nodes = [None] * len(lst)
        for i, chr in enumerate(lst):
            if chr != "#":
                lst[i] = TreeNode(int(chr))
            else:
                lst[i] = None
        # print(lst)
        i, j = 0, 1
        while j < len(lst) and i < len(lst):
            # print(i, j)
            if not lst[i]:
                i+= 1
                continue
            lst[i].left = lst[j]
            j+=1
            lst[i].right = lst[j]
            j+=1
            i+=1
        return lst[0]
        
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans