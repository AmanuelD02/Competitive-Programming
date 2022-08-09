"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return
        stack = [head]
        dummy = Node()
        dummy.next = head
        prev = dummy
        while stack:
            curr = stack.pop()
            prev.next = curr
            curr.prev = prev
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None
            
            prev = curr

        dummy.next.prev = None
        return dummy.next
            
            
            
            
        
            