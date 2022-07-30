class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
def findMergeNode(head1, head2):
    merged = SinglyLinkedListNode(node_data=1)
    start = merged
    print("Stat1")
    while(head1 and head2):
        if head1.data >= head2.data:
            merged.next = head2
            head2 = head2.next
        else:
            merged.next = head1
            head1  = head1.next
        merged = merged.next
    left = head1 if head1 else head2
    print("stat2")
    while(left):
        merged.next = left
        left = left.next
        merged = merged.next
    return start.next.val

merged = SinglyLinkedListNode(node_data=1)
d = SinglyLinkedListNode(node_data=merged)
r = SinglyLinkedListNode(node_data=d)
t = SinglyLinkedListNode(node_data=r)


oo = SinglyLinkedListNode(node_data=1)
p = SinglyLinkedListNode(node_data=oo)
k = SinglyLinkedListNode(node_data=p)
m = SinglyLinkedListNode(node_data=r)


print(findMergeNode(merged, oo))
