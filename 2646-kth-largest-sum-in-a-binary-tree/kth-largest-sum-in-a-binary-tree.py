# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque([root])
        level_sum = []

        while q:
            s = 0
            for _ in range(len(q)):
                node = q.popleft()
                s+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level_sum.append(s)
        level_sum.sort()
        return level_sum[-k] if len(level_sum)>=k else -1  