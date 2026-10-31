# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = float("-inf")
        self.postorder(root)
        return self.maxPath
    
    def postorder(self, root):
        if not root:
            return 0

        left = max(self.postorder(root.left), 0)
        right = max(self.postorder(root.right), 0)

        self.maxPath = max(self.maxPath, left + right + root.val)

        return max(left, right) + root.val


 