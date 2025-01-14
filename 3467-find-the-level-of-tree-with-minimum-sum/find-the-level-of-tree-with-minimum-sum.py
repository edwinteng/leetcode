# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumLevel(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        min_sum = float('Inf')
        level,min_level = 1,1
        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level_sum < min_sum:
                min_sum = level_sum
                min_level = level
            level+=1
        return min_level