# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left,right):
            if (left and not right) or (right and not left):
                return False
            if not left and not right:
                return True
            if left.val == right.val and dfs(left.right,right.left) and dfs(left.left,right.right):
                return True
            else:
                return False
        return dfs(root.left,root.right)