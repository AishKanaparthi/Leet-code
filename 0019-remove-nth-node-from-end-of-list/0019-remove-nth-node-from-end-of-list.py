

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        reversed_head = self.reverseList(head)
        
        # Handle case where the head itself needs to be removed
        if n == 1:
            return self.reverseList(reversed_head.next)
        
        # Find the nth node from the start (now nth node from the end in the reversed list)
        prev, curr = None, reversed_head
        for _ in range(n-1):
            prev, curr = curr, curr.next
        
        # Remove the nth node
        prev.next = curr.next
        
        # Reverse the list again to get the final result
        return self.reverseList(reversed_head)
