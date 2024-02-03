# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        a=[]
        q= collections.deque()
        if root:
            q.append(root)
        # q= deque([root])
        
        while q:
            b=[] 
            for i in range(len(q)):
               
                node= q.popleft()
                
                b.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            a.append(b)
        return a
                
                
        