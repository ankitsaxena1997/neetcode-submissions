# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter=0

        def dfs(node):

            if node==None:
                return 0
            
            left = 1+dfs(node.left)
            right = 1+dfs(node.right)

            self.diameter= max(self.diameter,left+right-2)

            return max(left,right)
        
        dfs(root)

        return self.diameter
