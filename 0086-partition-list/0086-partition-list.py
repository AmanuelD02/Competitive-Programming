# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lesser, greater = ListNode(-1, None), ListNode(-1, None)
        
        start = head
        less, great = lesser, greater
        while start:
            if start.val < x:
                lesser.next = start
                lesser = lesser.next
            else:
                greater.next = start
                greater = greater.next
            start = start.next
        
        greater.next = None
        lesser.next = great.next
        
        return less.next
        