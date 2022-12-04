# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        
        mid = self.findMid(head)
        tmp = mid.next
        mid.next = None
        right = tmp
        
 
        # Divide 
        leftSide = self.sortList(head)
        rightSide = self.sortList(right)
        
        # Merge
        head = self.merge(leftSide, rightSide)
        
        return head
    
    
    
    
    def findMid(self, head):
        slow = fast = head
        fast = fast.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def merge(self, l1, l2):
        curr = dummy = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        
        return dummy.next