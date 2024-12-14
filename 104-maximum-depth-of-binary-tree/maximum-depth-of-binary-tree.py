# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            if root.left is None and root.right is None:
                return 1
            if root.left is None:
                return dfs(root.right)+1
            if root.right is None:
                return dfs(root.left)+1
            return max(dfs(root.left),dfs(root.right))+1
        return dfs(root)