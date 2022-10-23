# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        
        curr, prev = head, None
        for _ in range(left - 1):
            prev = curr
            curr = curr.next
        
        con, tail = prev, curr
        for _ in range(right - left+1):
            third= curr.next
            curr.next = prev
            prev = curr
            curr = third
        
        if con:
            con.next = prev
        else:
            head = prev
            
        tail.next = curr
        
        return head
            