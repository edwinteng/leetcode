class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        num_row,num_col = len(obstacleGrid),len(obstacleGrid[0])
        grid = [[0]*num_col for i in range(num_row)]
        for i in range(num_row):
            if obstacleGrid[i][0]==1:
                break
            grid[i][0] = 1 
        for j in range(num_col):
            if obstacleGrid[0][j]==1:
                break
            grid[0][j] = 1

        for i in range(1,num_row):
            for j in range(1,num_col):
                if obstacleGrid[i][j]==1:
                    grid[i][j] = 0
                else:           
                    grid[i][j]=grid[i][j-1]+grid[i-1][j] 
                    
        #print(grid)
        return grid[num_row-1][num_col-1]