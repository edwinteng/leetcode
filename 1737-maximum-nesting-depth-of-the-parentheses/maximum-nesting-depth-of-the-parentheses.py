class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max_depth,depth = 0,0
        for c in s:
            if c =='(':
                stack.append('(')
                depth+=1
                max_depth = max(max_depth,depth)
            elif c==')':
                stack.pop()
                depth-=1
        return max_depth