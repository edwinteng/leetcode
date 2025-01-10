# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if not root or root == p or root==q:
                return root
            left_child = dfs(root.left)
            right_child = dfs(root.right)
            if left_child and right_child:
                return root
            return left_child or right_child
        return dfs(root)