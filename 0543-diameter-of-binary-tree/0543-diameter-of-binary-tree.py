class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxDepth(node):
            if not node:
                return 0
            left_depth = maxDepth(node.left)
            right_depth = maxDepth(node.right)
            
            self.diameter = max(self.diameter, left_depth + right_depth)
            # Return the max depth of the current subtree
            return 1 + max(left_depth, right_depth)

        self.diameter = 0  # Initialize diameter as a class variable
        maxDepth(root)
        return self.diameter

        
            
        