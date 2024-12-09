# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root_p,root_q):
            if root_p is None and root_q is None:
                return True
            #check root_p.val and 
            if root_p is None and root_q is not None:
                return False
            if root_p is not None and root_q is None:
                return False
            return root_p.val==root_q.val and dfs(root_p.left,root_q.left) and dfs(root_p.right,root_q.right)
        return dfs(p,q)