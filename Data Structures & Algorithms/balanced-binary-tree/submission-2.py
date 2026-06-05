# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root==None:
            return True

        if abs(self.depth(root.left)-self.depth(root.right))>1:
            return False
        
        return self.isBalanced(root.right) and self.isBalanced(root.left)
    
    def depth(self, root: Optional[TreeNode]) -> int:

        if root==None:
            return 0
        
        depth_left = 1+self.depth(root.left)
        depth_right= 1+self.depth(root.right)

        return max(depth_left,depth_right)
        