class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        ans = ['']*numRows
        direction = 1
        index = 0
        for c in s:
            ans[index]+=c
            if index==numRows-1:
                direction=-1
            if index==0:
                direction =1
            index+=direction
        return ''.join(ans)


