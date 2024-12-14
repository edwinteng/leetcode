# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(root,path,cur_sum):
            if not root:
                return
            #if root.left:
            if root.left is None and root.right is None and cur_sum+root.val== targetSum:
                    ans.append(path+[root.val])
            dfs(root.left,path+[root.val],cur_sum+root.val)
            #if root.right:
            dfs(root.right,path+[root.val],cur_sum+root.val)
        dfs(root,[],0)
        return ans