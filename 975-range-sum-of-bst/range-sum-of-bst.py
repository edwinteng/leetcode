# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        #total = 0
        def dfs(root):
            if not root:
                return 0
            if low<=root.val<=high:
                left =dfs(root.left)
                right = dfs(root.right)
                return root.val+left+right
            elif root.val < low:
                return dfs(root.right)
            elif root.val > high:
                return dfs(root.left)
            
        return dfs(root)