# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        def dfs(root,path):
            if not root:
                return
            if not root.left and not root.right:
                ans.append(path+[str(root.val)])
                return
            dfs(root.left,path+[str(root.val)])
            dfs(root.right,path+[str(root.val)])
        dfs(root,[])
        total=0
        for num_list in ans:
            total+=int(''.join(num_list))
        return total
