# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                break
        
        if not (fast and fast.next):
            return None
        
        index = 0
        while head != slow:
            head = head.next
            slow = slow.next
            index += 1
        
        return head