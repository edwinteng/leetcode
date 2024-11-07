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
        ans = []
        #print(q)
        while q:
            n = len(q)
            print(n)
            level = []
            for i in range(n):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(level[-1])
        return ans

        