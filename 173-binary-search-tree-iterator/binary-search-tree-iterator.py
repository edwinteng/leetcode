# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root=root.left
        
    def next(self):
        """
        :rtype: int
        """
        this_node = self.stack.pop()
        node = this_node.right
        while node:
            self.stack.append(node)
            node = node.left
        return this_node.val     

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.stack)>0:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()