# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a= []
        
        prev, curr = None, head
        
        while curr:
            
            if(curr in a):
                return True
            else:
                a.append(curr)
            curr= curr.next
        return False
        
        