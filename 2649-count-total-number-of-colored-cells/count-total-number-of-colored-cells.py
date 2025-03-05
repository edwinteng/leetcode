class Solution:
    def coloredCells(self, n: int) -> int:
        
        #2* (n-1)*(1+(2*(n-1)-1))/2+(n*2)-1
        #2*(n-1)(n-1)+(n*2)-1
        #2(n^2-2n+1)+2n-1
        #2n^2 +2n-1
        return 2*n*n-2*n+1