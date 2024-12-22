# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root):
            if not root:
                return -1
            nonlocal ans
            h_left = dfs(root.left)
            h_right = dfs(root.right)
            ans = max(ans,h_left+h_right+2)
            h = max(h_left,h_right)+1
            return h
        dfs(root)
        return ans