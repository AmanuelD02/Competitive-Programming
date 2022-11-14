# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        dummy = ListNode(-1, head)
        start = end =  head
        steps = k - 1
        
        while end and steps:
            end = end.next
            steps -= 1
    
        if end:
            # REVERSE and CALL REVERSE K GROUP for the remaining part
            prev = self.reverseKGroup(end.next, k)
            curr = start
            for _ in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                          
            return end
                
            
        else:
            return dummy.next