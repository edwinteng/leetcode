# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        q = deque([root])
        ans = [root.val]
        while q:

            
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    level.append(node.left.val)
                    q.append(node.left)
                if node.right:
                    level.append(node.right.val)
                    q.append(node.right)
            #if len(level)>0:
            #print(level)
            if level:
                ans.append(max(level))
        return ans

