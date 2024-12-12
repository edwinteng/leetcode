# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        #0,0,3     x (parent assign),y(level)  

        queue=deque()
        
        level = 0
        d = {}
        queue.append((0,root))
        while len(queue)>0:
            x,node = queue.popleft()
            if not node:
                return []
            d[x] = d.get(x,[])
            d[x].append(node.val)
            if node.left:
                queue.append((x-1,node.left))
            if node.right:
                queue.append((x+1,node.right))
        print(d)
        return [ value for _,value in sorted(d.items())]


                
