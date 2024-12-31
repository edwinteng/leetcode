# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=deque([(0,root)])
        d = {}

        while q:
            x,node = q.popleft()

            d[x]=d.get(x,[])
            d[x].append(node.val)
            if node.left:
                q.append((x-1,node.left))
            if node.right:
                q.append((x+1,node.right))
        return [val for key,val in sorted(d.items())]


        
        

