# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a= set()
        tail = head
        
        while tail:
            if tail in a:
                return True
            else:
                a.add(tail)
            tail= tail.next
        