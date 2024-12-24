# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #queue
        # put root node into the queue
        if root is None:
            return []
        q = deque([root])
        ans= []
        while q:
            n = len(q)
            level_q = []
            for _ in range(n):
                node = q.popleft()
                level_q.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level_q[-1].val)
        return ans
        