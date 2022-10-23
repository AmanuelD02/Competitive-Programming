# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(0,head)
        curr, prev = head, dummy
        for _ in range(left - 1):
            prev = curr
            curr = curr.next
        
        con, tail = prev, curr
        for _ in range(right - left+1):
            third= curr.next
            curr.next = prev
            prev = curr
            curr = third
        
        
        con.next = prev
    
        tail.next = curr
        
        return dummy.next
            