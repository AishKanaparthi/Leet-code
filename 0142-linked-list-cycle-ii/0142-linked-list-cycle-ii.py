# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=set()
        tail=head
        
        while tail:
            if tail in a:
                return tail
            else:
                a.add(tail)
            tail = tail.next
        