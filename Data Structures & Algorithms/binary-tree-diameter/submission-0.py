# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0
        
        r= self.diameterOfNode(root)
        branch_max=max(self.diameterOfBinaryTree(root.left) , self.diameterOfBinaryTree(root.right))

        return max(r,branch_max)

    def diameterOfNode(self, root: Optional[TreeNode]) -> int:

        if root == None or (root.left==None and root.right==None):
            return 0
        
        if root.left==None:
            return 1+self.maxDepth(root.right)
        
        if root.right==None:
            return 1+self.maxDepth(root.left)

        return 2 + self.maxDepth(root.right)+self.maxDepth(root.left)

    
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root == None :
            return -1
        
        leftDepth = 1+ self.maxDepth(root.left)
        rightDepth = 1+ self.maxDepth(root.right)

        return max(leftDepth , rightDepth)
        