# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            if root.left and root.right:
                return min(dfs(root.left),dfs(root.right))+1
            if root.left:
                return dfs(root.left)+1
            if root.right:
                return dfs(root.right)+1
        return dfs(root)