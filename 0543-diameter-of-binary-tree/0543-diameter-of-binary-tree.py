# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
        
#         return 1+ max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res= [0]
        
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res[0]= max(res[0], left +right+2)
            h= 1+max(left, right)
            return h
        dfs(root)
        return res[0]
        
        