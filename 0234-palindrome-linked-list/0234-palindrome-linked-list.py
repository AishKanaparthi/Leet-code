# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast= head, head.next
        
        while fast and fast.next:
            slow= slow.next 
            fast= fast.next.next
            
        second = slow.next
        prev = slow.next = None
        
        while second:
            temp = second.next
            second.next = prev
            prev= second 
            second = temp
            
        first,second = head, prev
        
        while first and second:
            if(first.val != second.val):
                return False
            
            else:
                first,second = first.next,second.next
        return True
            
            
        
        
        
        
        
        
        
        
        
    
        