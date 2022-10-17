# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        
        odd, even = head, head.next
        odd_t, even_t = odd, even
        while even_t and even_t.next:
            odd_t.next = even_t.next
            odd_t = odd_t.next
            
            tmp = even_t.next
            even_t.next = tmp.next
            even_t = even_t.next
        
        odd_t.next = even
        
        return odd