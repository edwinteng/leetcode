# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        max_level_sum = float('-Inf')
        max_level = 1
        level = 1
        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level_sum > max_level_sum:
                max_level_sum = level_sum
                max_level = level
            level+=1
        return max_level
        