class Solution:
    def maxDepth(self, s: str) -> int:
        num_left = 0
        ans = 0
        for c in s:
            if c == '(':
                num_left+=1
                ans = max(num_left,ans)
            elif c == ')':
                num_left-=1
            else:
                continue
        return ans