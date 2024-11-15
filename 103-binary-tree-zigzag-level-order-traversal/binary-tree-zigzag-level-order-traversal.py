# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is  None:
            return []
        ans = []
        queue = deque([root])
        direction = 1
        while len(queue)>0:
            n = len(queue)
            level = []
            for _ in range(n):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if direction == 1:
                ans.append(level)
            else:
                ans.append(level[::-1])
            direction = -direction
        return ans