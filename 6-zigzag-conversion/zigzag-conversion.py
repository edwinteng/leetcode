class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s)< numRows:
            return s
        ans = ['' for i in range(numRows)]
        direction,row = 1,0
        for char in s:
            ans[row]+=char 
            if row==numRows-1:
                direction=-1
            if row==0:
                direction=1
            row+=direction
        return ''.join(ans)