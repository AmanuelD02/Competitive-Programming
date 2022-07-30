# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        slow = fast = first = dummy
        
        for i in range(k):
            fast = fast.next
            first = first.next
            
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.val, first.val = first.val, slow.val
        return dummy.next
        
            