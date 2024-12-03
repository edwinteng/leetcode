# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(root,path):
            if root is None:
                #allpath.append('->'.join(path))
                return
            else:
                #path.append(str(root.val))
                if root.left is None and root.right is None:
                    allpath.append('->'.join(path+[str(root.val)]))
                else:
                    dfs(root.left,path + [str(root.val)])
                    dfs(root.right,path + [str(root.val)])
                #path.pop()
        allpath = []
        
        dfs(root,[])
        return allpath