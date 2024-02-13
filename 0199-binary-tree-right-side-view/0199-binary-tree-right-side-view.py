# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        q = collections.deque([root])

        while q:
            rightSide = None

            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res

        #         curr = root
        
#         while curr or stack:
#             while curr:
#                 stack.append(curr)
#                 curr = curr.right
                
#             curr = stack.pop()
#             res.append(curr.val)
#             curr = curr.left
#         return res[::-1]
        
#         curr = root
        
#         while curr or stack:
#             while curr:
#                 stack.append(curr)
#                 curr = curr.right
                
#             curr = stack.pop()
#             res.append(curr.val)
#             curr = curr.left
#         return res[::-1]
        
        
            
            