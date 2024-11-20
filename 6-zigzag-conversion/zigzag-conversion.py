class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = ['' for i in range(numRows)]
        
        row = 0
        delta = 1
        for i in range(len(s)):
            ans[row]=ans[row]+s[i]
            if row == numRows-1:
                delta=-1
            if row == 0:
                delta = 1
            row = row+delta
        return ''.join(ans)
