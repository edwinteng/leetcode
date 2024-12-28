# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        q = deque([(0,0,root)])
        arr= [(0,0,root.val)]
        while q:
            row,col,node = q.popleft()
            if node.left:
                q.append((row+1,col-1,node.left))
                arr.append((row+1,col-1,node.left.val))
            if node.right:
                q.append((row+1,col+1,node.right))
                arr.append((row+1,col+1,node.right.val))
        arr.sort(key=lambda x: (x[1],x[0],x[2]))
        print(arr)
        ans = []
        prev = float('Inf')
        for row,col,val in arr:
            if prev !=col:
                ans.append([])
                prev = col
            ans[-1].append(val)
        return ans


