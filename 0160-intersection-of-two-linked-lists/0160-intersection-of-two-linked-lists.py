class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        setA = set()

        # Traverse the first linked list and store its nodes in a set
        while headA:
            setA.add(headA)
            headA = headA.next

        # Traverse the second linked list and check if any node is in the set
        while headB:
            if headB in setA:
                return headB
            headB = headB.next

        return None  # Return None if no intersection is found
