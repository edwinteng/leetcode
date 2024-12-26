# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder or not postorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder)>1:
            left_root = preorder[1]
            left_root_index = postorder.index(left_root)
            size_left_tree = left_root_index+1
            root.left = self.constructFromPrePost(preorder[1:size_left_tree+1],postorder[:size_left_tree])
            root.right = self.constructFromPrePost(preorder[(size_left_tree+1):],postorder[size_left_tree:-1])
        return root