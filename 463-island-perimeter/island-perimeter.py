class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        num_row,num_col=len(grid),len(grid[0])
        for i in range(num_row):
            for j in range(num_col):
                if grid[i][j]==1:
                    for d_i,d_j in [(0,1),(1,0),(0,-1),(-1,0)]:
                        cur_i,cur_j = i+d_i,j+d_j
                        if 0<=cur_i<num_row and 0<=cur_j<num_col and grid[cur_i][cur_j]==1:
                            ans-=1
                    ans+=4
        return ans